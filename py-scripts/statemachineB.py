#!/bin/python2.7

from naoqi import ALProxy
import sys
import time
import pandas as pd # Needed for gathering data and writing to csv
from enum import Enum

#ip = "192.168.208.210" # Change based on session
#port = 9559

ip = str(sys.argv[1])
port = int(sys.argv[2])

# Constants
DEFAULT_MEM = ['', -3.0]
#FILE = "mainResultsB.csv"
FILE = str(sys.argv[3])
DELAY=1.5
VOL=1.0

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
    speechRec.pause(True)
    speechRec.setVocabulary(vocab, wordSpot)
    
    speechRec.subscribe("RobotB")
    response = DEFAULT_MEM
    counter = 0

    # Keep checking until the response changes or 5 seconds has elapsed
    while response == DEFAULT_MEM and counter < 500:
        time.sleep(0.01)
        # Check memory for the word
        response = mem.getData("WordRecognized")
        counter += 1
    speechRec.unsubscribe("RobotB")
    print("RESPONSE = %s" % response)

    # Record word and confidence data
    word_list.append(response[0])
    conf_list.append(response[1])

    if response == DEFAULT_MEM:
        return False
    else:
        return True

# state 0 - initialize robot
state = 0
word_list = [DEFAULT_MEM[0]]
conf_list = [DEFAULT_MEM[1]]

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
#        animSay.setParameter("pitch", 2.0)
        state = 1
    elif state == 1:
        animSay.say("\\vct=0\\Why are you ignoring me? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        time.sleep(DELAY)
        animSay.say("\\vct=0\\Do you want ice cream? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        time.sleep(DELAY)
        animSay.say("\\vct=0\\Do you want to play a game? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        time.sleep(DELAY)
        animSay.say("\\vct=0\\Are you tired? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        time.sleep(DELAY)
        animSay.say("\\vct=0\\What is wrong? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        leds.fadeRGB(ledsGroup, Color.BLUE, 0.1)
        time.sleep(DELAY)
        state = 2
    elif state == 2:
        animSay.say("\\vct=0\\Cheer up. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        if recSpeech(['are', 'you']):
            state = 3
        else:
            state = 2
    elif state == 3:
        time.sleep(DELAY)
        animSay.say("\\vct=0\\Everything will get better with time. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        if recSpeech(['eyes', 'blue']):
            state = 4
        else:
            state = 3
    elif state == 4:
        time.sleep(DELAY)
        animSay.say("\\vct=0\\Do you want to hear a joke? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        if recSpeech(['affirmative']):
            state = 5
        else:
            state = 4
    elif state == 5:
        time.sleep(DELAY)
        animSay.say("\\vct=0\\What is nine plus ten? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        if recSpeech(['twenty', 'one']):
            animSay.say("\\vct=0\\Good answer. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
            leds.fadeRGB(ledsGroup, Color.RED, 0.1)
            print("DONE")
            break
        else:
            state = 5

d = {'word':word_list, 'confidence':conf_list}
df = pd.DataFrame(d)
df.to_csv(FILE)
