#!/bin/python2.7

from naoqi import ALProxy
import sys
import time
from enum import Enum

# Change when applicable
ip = "169.254.211.101"
port = 9559

# Constants
DEFAULT_MEM = ['', -3.0]

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
    dialog = ALProxy("ALDialog", ip, port)

    dialog.setLanguage("English")
    # Robot B: hello
    # Robot A: hi
    # Robot B: propose
    # Robot A: rejection
    # Robot B: game
    # Robot A: accept
    # Robot B: explainGame
    topicContent = ("topic: ~mytopic()\n"
                    "language: enu\n"
                    "concept:(greetings) ^rand[hi hello \"hey there\"]\n"
                    "concept:(propose) ^rand[\"Did you hear me?\" \"Are you okay?\" \"Do you want ice cream?\"]\n"
                    "concept:(rejections) ^rand[Nope Nah \"You are going to have to do better than that.\"]\n"
                    "concept:(accept) ^rand[Yes Okay \"I'd like that.\"]\n"
                    "concept:(game) \"Do you want to play a game?\"\n"
                    "dynamic: gameAns\n"
                    "proposal: hello\n"
                    "proposal: %pro ~propose\n"
                    "proposal: ~game\n"
                    "u:(^empty) ^nextProposal\n"
                    "u:(~rejections) ^gotoReactivate(pro)\n"
                    "\n"
#                    "u: (~greetings) ~greetings\n"
                    )
    topicName = dialog.loadTopicContent(topicContent)
    dialog.activateTopic(topicName)
    dialog.subscribe("TestDialog")
                    
except:
    print("ERROR")
    sys.exit()

def robotA():
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
    # begin recognizing speech
    recSpeech(['ignoring', 'me'])
    recSpeech(['ice', 'cream'])
    recSpeech(['a', 'game'])
    recSpeech(['you', 'tired'])
    recSpeech(['is', 'wrong'])
    leds.fadeRGB(ledsGroup, Color.BLUE, 0.1)
    recSpeech(['cheer', 'up'])
    animSay.say("How are you? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    recSpeech(['with', 'time'])
    animSay.say("Why are your eyes blue? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    recSpeech(['a', 'joke'])
    animSay.say("Affirmative. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    recSpeech(['nine', 'ten'])
    animSay.say("Twenty-one. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    recSpeech(['good', 'answer'])
    leds.fadeRGB(ledsGroup, Color.GREEN, 0.1)

def robotB():
    # stand up
    posture.goToPosture("StandInit", 1.0)
    # eye color
    ledsGroup = "eyes"
    ledsNames = ["FaceLeds"]
    leds.createGroup(ledsGroup, ledsNames)
    leds.on(ledsGroup)
    leds.fadeRGB(ledsGroup, Color.GREEN, 0.1)
    # set speaker volume
    tts.setVolume(1.0)
    # begin recognizing speech
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
    animSay.say("Cheer up. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    recSpeech(['are', 'you'])
    animSay.say("Everything will get better with time. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    recSpeech(['eyes', 'blue'])
    animSay.say("Do you want to hear a joke? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    recSpeech(['affirmative'])
    animSay.say("What is nine plus ten? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    recSpeech(['twenty', 'one'])
    animSay.say("Good answer. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    leds.fadeRGB(ledsGroup, Color.RED, 0.1)

def recSpeech(vocab, wordSpot=True):
    #tts.say("Hello")
    speechRec.pause(True)
    speechRec.setVocabulary(vocab, wordSpot)
    
    speechRec.subscribe("Test")
    response = DEFAULT_MEM
    while response == DEFAULT_MEM:
        time.sleep(1)
        response = mem.getData("WordRecognized")
        print("RESPONSE = %s" % response)
    speechRec.unsubscribe("Test")
    tts.say("%s" % response)
