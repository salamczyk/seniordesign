#!/bin/python2.7

from naoqi import ALProxy
import sys
import time
from enum import Enum

ip = "1" # change
port = 9559

# Constants
DEFAULT_MEM = ['', -3.0]
FILE = "mainResultsA.csv"

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
    sys.exit()

def recSpeech(vocab, wordSpot=True):
    speechRec.pause(True)
    speechRec.setVocabulary(vocab, wordSpot)
    
    speechRec.subscribe("RobotA")
    response = DEFAULT_MEM
    counter = 0
    
    while response == DEFAULT_MEM and counter < 50:
        time.sleep(0.01)
        response = mem.getData("WordRecognized")
        counter += 1
    speechRec.unsubscribe("RobotA")
    print("RESPONSE = %s" % response)
    print("MOOD = %s" % mood_rating)

    # with open(FILE, 'a') as f:
    #     f.write('RESPONSE = ' + str(response))
    #     f.write('\n')
    #     f.write('MOOD = ' + str(mood_rating))
    #     f.write('\n')

    word_list.append(response[0])
    conf_list.append(response[1])

    if response == DEFAULT_MEM:
        mood_list.append(mood_rating)
        return False
    else:
        mood_rating += 20
        mood_list.append(mood_rating)
        if mood_rating >= 100:
            leds.fadeRGB(ledsGroup, Color.GREEN, 0.1)
        elif mood_rating >= 0:
            leds.fadeRGB(ledsGroup, Color.BLUE, 0.1)
        else:
            leds.fadeRGB(ledsGroup, Color.RED, 0.1)
        return True

# state 0 - initialize robot
state = 0
mood_list = [-100]
word_list = [DEFAULT_MEM[0]]
conf_list = [DEFAULT_MEM[1]]

while True:    
    if state = 0:
        # stand up
        posture.goToPosture("StandInit", 1.0)
        # eye color
        ledsGroup = "eyes"
        ledsNames = ["FaceLeds"]
        leds.createGroup(ledsGroup, ledsNames)
        leds.on(ledsGroup)
        leds.fadeRGB(ledsGroup, Color.RED, 0.1)
        # set speaker volume
        tts.setVolume(1.0)
        mood_rating = -100
        state = 1
    elif state = 1:
        # begin recognizing speech
        recSpeech(['ignoring', 'me'])
        recSpeech(['ice', 'cream'])
        recSpeech(['a', 'game'])
        recSpeech(['you', 'tired'])
        recSpeech(['is', 'wrong'])
        recSpeech(['cheer', 'up'])
        state = 2
    elif state = 2:
        time.sleep(1)
        animSay.say("How are you? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        if recSpeech(['with', 'time']):
            state = 3
        else:
            state = 2
    elif state = 3:
        time.sleep(1)
        animSay.say("Why are your eyes blue? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        if recSpeech(['a', 'joke']):
            state = 4
        else:
            state = 3
    elif state = 4:
        time.sleep(1)
        animSay.say("Affirmative. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        if recSpeech(['nine', 'ten']):
            state = 5
        else:
            state = 4
    elif state = 5:
        time.sleep(1)
        animSay.say("Twenty-one. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        if recSpeech(['good', 'answer']):
            print("DONE")
            break
        else:
            state = 5

d = {'word':word_list, 'confidence':conf_list, 'mood':mood_list}
df = pd.DataFrame(d)
df.to_csv(FILE)
