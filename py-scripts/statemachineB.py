#!/bin/python2.7

from naoqi import ALProxy
import sys
import time
from enum import Enum

ip = "1" # change
port = 9559

# Constants
DEFAULT_MEM = ['', -3.0]
FILE = "mainResultsB.out"

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
    
    speechRec.subscribe("Test")
    response = DEFAULT_MEM
    counter = 0
    
    while response == DEFAULT_MEM and counter < 50:
        time.sleep(0.01)
        response = mem.getData("WordRecognized")
        counter += 1
    speechRec.unsubscribe("Test")
    print("RESPONSE = %s" % response)

    with open(FILE, 'a') as f:
        f.write('RESPONSE = ' + str(response))
        f.write('\n')

    if response == DEFAULT_MEM:
        return False
    else:
        return True

# state 0 - initialize robot
state = 0

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
        state = 1
    elif state = 1:
        animSay.say("Why are you ignoring me? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        time.sleep(1)
        animSay.say("Do you want ice cream? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        time.sleep(1)
        animSay.say("Do you want to play a game? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        time.sleep(1)
        animSay.say("Are you tired? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        time.sleep(1)
        animSay.say("What is wrong? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        leds.fadeRGB(ledsGroup, Color.BLUE, 0.1)
        time.sleep(1)
        state = 2
    elif state = 2:
        animSay.say("Cheer up. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        if recSpeech(['are', 'you']):
            state = 3
        else:
            state = 2
    elif state = 3:
        time.sleep(1)
        animSay.say("Everything will get better with time. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        if recSpeech(['eyes', 'blue']):
            state = 4
        else:
            state = 3
    elif state = 4:
        time.sleep(1)
        animSay.say("Do you want to hear a joke? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        if recSpeech(['affirmative']):
            state = 5
        else:
            state = 4
    elif state = 5:
        time.sleep(1)
        animSay.say("What is nine plus ten? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
        if recSpeech(['twenty', 'one']):
            animSay.say("Good answer. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
            leds.fadeRGB(ledsGroup, Color.RED, 0.1)
            print("DONE")
            sys.exit()
        else:
            state = 5
