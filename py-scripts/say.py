from naoqi import ALProxy
import time


ip = "192.168.208.210" # change
port = 9559

animSay = ALProxy("ALAnimatedSpeech", ip, port)

for i in range(100):
    animSay.say("Why are you ignoring me. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    time.sleep(1)
    animSay.say("Do you want ice cream? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    time.sleep(1)
    animSay.say("Do you want to play a game? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    time.sleep(1)
    animSay.say("Are you tired? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    time.sleep(1)
    animSay.say("What is wrong? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    time.sleep(1)
    animSay.say("Cheer up. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    time.sleep(1)
    animSay.say("Everything will get better with time. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    time.sleep(1)
    animSay.say("Do you want to hear a joke? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    time.sleep(1)
    animSay.say("What is nine plus ten? ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    time.sleep(1)
    animSay.say("Good answer. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    time.sleep(1)
    animSay.say("How are you. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    time.sleep(1)
    animSay.say("Why are your eyes blue. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    time.sleep(1)
    animSay.say("Affirmative. ^start(animations/Stand/Gestures/Hey_2)", "contextual")
    time.sleep(1)
    animSay.say("twenty one. ^start(animations/Stand/Gestures/Hey_2)", "contextual")

    time.sleep(1)