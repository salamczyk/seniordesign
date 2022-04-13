from naoqi import ALProxy
import random
import time
import sys
import os

def start():
    tts.say("hello")
    speechRecProxy.pause(True)
    speechRecProxy.setVocabulary(['hello', 'hi'], True)
    speechRecProxy.subscribe("Test")

    response = ['', -3.0]
    while response == ['', -3.0]:
        time.sleep(1)
        response = memProxy.getData("WordRecognized")
        print(response)
    tts.say(response)
    speechRecProxy.unsubscribe("Test")

arg0 = os.path.basename(sys.argv[0]).split('.')[0]

ip = "169.254.44.50"

try:
    speechRecProxy = ALProxy("ALSpeechRecognition", ip, 9559)
    tts = ALProxy("ALTextToSpeech", ip, 9559)
    memProxy = ALProxy("ALMemory", ip, 9559)
except:
    print("ERROR")
    sys.exit()

speechRecProxy.setLanguage("English")

start()

