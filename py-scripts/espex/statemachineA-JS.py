#!/bin/python2.7

from naoqi import ALProxy
import sys
import time
import math
import pandas as pd # Needed for gathering data and writing to csv
from enum import Enum
from vocab import *

#ip = "192.168.208.177" # Change based on session
#port = 9559
ip = str(sys.argv[1])
port = int(sys.argv[2])
mood_rating = -100

# Constants
DEFAULT_MEM = ['', -3.0]
FILE = str(sys.argv[3])
DELAY=1.5/2.0
VOL=1.0

if str(sys.argv[4]) == 'espex':
    DIALOG = espexDialog
    VOCAB = espexVocab
else:
    DIALOG = pilotDialog
    VOCAB = pilotVocab

CHANGE = math.ceil(200.0/len(DIALOG[1]))

# Enumeration to make colors more readable
class Color(Enum):
    RED = 0x00ff0000
    GREEN = 0x0000ff00
    BLUE = 0x000000ff

# import proxies to control robot
try:
    speechRec = ALProxy("ALSpeechRecognition", ip, port)
    tts = ALProxy("ALTextToSpeech", ip, port)
    animSay = ALProxy("ALAnimatedSpeech", ip, port)
    mem = ALProxy("ALMemory", ip, port)
    leds = ALProxy("ALLeds", ip, port)
    posture = ALProxy("ALRobotPosture", ip, port)
except:
    print("ERROR")
    sys.exit(1)

def recSpeech(vocab, wordSpot=True):
    """
    Recognizes speech using speech recognition and memory proxies.
    
    Parameters:
        vocab - List of words to be recognized;
        wordSpot - Whether the NAO can recognize it in a phrase/sentence;
    
    Returns:
        True if speech was recognized, False after 5 seconds and nothing recognized
    """
    global mood_rating
    speechRec.pause(True)
    speechRec.setVocabulary(vocab, wordSpot)
    
    speechRec.subscribe("RobotA")
    response = DEFAULT_MEM
    counter = 0

    # Keep checking until the response changes or 5 seconds has elapsed
    while response == DEFAULT_MEM and counter < 500:
        time.sleep(0.01)
        # Check memory for the word
        response = mem.getData("WordRecognized")
        counter += 1
    speechRec.unsubscribe("RobotA")
    print("RESPONSE = %s" % response)
    print("MOOD = %s" % mood_rating)

    # Record word and confidence data
    word_list.append(response[0])
    conf_list.append(response[1])

    # Keep mood rating constant if nothing recognized
    # else increase mood rating by 20
    if response == DEFAULT_MEM:
        mood_list.append(mood_rating)
        return False
    else:
        mood_rating += CHANGE
        # Eye color is varied depending on mood rating
        # Since vision recognition isn't implemented this is more
        # of an indication of the robot's mood
        if mood_rating >= 100:
            mood_rating = 100
            leds.fadeRGB(ledsGroup, Color.GREEN, 0.1)
        elif mood_rating >= 0:
            leds.fadeRGB(ledsGroup, Color.BLUE, 0.1)
        else:
            leds.fadeRGB(ledsGroup, Color.RED, 0.1)
        mood_list.append(mood_rating)
        return True

# state 0 - initialize robot
state = 0
i = 0 # dialog counter
j = 0 # vocab counter
mood_list = [-100]
word_list = [DEFAULT_MEM[0]]
conf_list = [DEFAULT_MEM[1]]

# State-machine style approach
while True:    
    if state == 0:
        # stand up
        posture.goToPosture("StandInit", 1.0)
        # eye color
        ledsGroup = "eyes"
        ledsNames = ["FaceLeds"]
        leds.createGroup(ledsGroup, ledsNames)
        leds.on(ledsGroup)
        leds.fadeRGB(ledsGroup, Color.RED, 0.1)
        # set speaker volume
        tts.setVolume(VOL)
        state = 1
    elif state == 1:
        # begin recognizing speech
        while mood_rating < 0:
            if recSpeech(VOCAB[0][j]):
                j += 1
        state = 2
    elif state == 2:
        time.sleep(DELAY)
        animSay.say(DIALOG[0][i])
        while mood_rating < 100:
            if recSpeech(VOCAB[0][j]):
                i += 1
                j += 1
                time.sleep(DELAY)
                animSay.say(DIALOG[0][i])
        print("DONE")
        break

# Writing to csv for later processing
d = {'word':word_list, 'confidence':conf_list, 'mood':mood_list}
df = pd.DataFrame(d)
df.to_csv(FILE)
