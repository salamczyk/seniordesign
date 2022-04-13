#!/bin/python2.7

from naoqi import ALProxy
import sys
import time
import pandas as pd
from enum import Enum

# Change when applicable
ip = "169.254.245.88"
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
except:
    print("ERROR")
    sys.exit()

def recSpeech(vocab, wordSpot=True):
    #tts.say("Hello")
    speechRec.pause(True)
    speechRec.setVocabulary(vocab, wordSpot)
    
    speechRec.subscribe("recordTrials")
    response = DEFAULT_MEM
    counter = 0
    
    while response == DEFAULT_MEM and counter < 50:
        time.sleep(0.01)
        response = mem.getData("WordRecognized")
        counter += 1
    speechRec.unsubscribe("recordTrials")
    print("RESPONSE = %s" % response)
    return response
    #tts.say("%s" % response)
#robotA()

def record_trials(vocab, fileName, numTrials):

    count = 0
    conf_list = []
    word_list = []

    while count < numTrials:
        result = recSpeech(vocab)
        if result[1] != -3.0:
            count += 1
            conf_list.append(result[0])
            word_list.append(result[1])

    print conf_list
    print word_list

    d = {'word':word_list, 'confidence':conf_list}

    df = pd.DataFrame(d)
    df.to_csv(fileName, index=False)

    # with open(fileName, 'a') as f:
    #     f.write(str(word_list))
    #     f.write('\n')
    #     f.write(str(conf_list))
    #     f.write('\n')
