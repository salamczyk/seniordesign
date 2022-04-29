#!/bin/python2.7

pilotDialog = [
    # Robot A lines
    ["\\vct=100\\How are you? ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=100\\Why are your eyes blue? ^start(animations/Stand/Gestures/Hey_1)",
     "\\vct=100\\Affirmative. ^start(animations/Stand/Gestures/Hey_3)",
     "\\vct=100\\Twenty-one. ^start(animations/Stand/Gestures/Hey_4)"
    ],
    # Robot B lines
    ["\\vct=0\\Why are you ignoring me? ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=0\\Do you want ice cream? ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=0\\Do you want to play a game? ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=0\\Are you tired? ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=0\\What is wrong? ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=0\\Cheer up. ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=0\\Everything will get better with time. ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=0\\Do you want to hear a joke? ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=0\\What is nine plus ten? ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=0\\Good answer. ^start(animations/Stand/Gestures/Hey_2)"
    ]
]

pilotVocab = [
    [['ignoring', 'me'],
     ['ice', 'cream'],
     ['a', 'game'],
     ['you', 'tired'],
     ['is', 'wrong'],
     ['cheer', 'up'],
     ['with', 'time'],
     ['a', 'joke'],
     ['nine', 'ten'],
     ['good', 'answer']
    ],
    [['are', 'you'],
     ['eyes', 'blue'],
     ['affirmative'],
     ['twenty', 'one']
    ]
]

espexDialog = [
    # Robot A lines
    ["\\vct=100\\What kind of game is it? ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=100\\How do I play? ^start(animations/Stand/Gestures/Hey_1)",
     "\\vct=100\\Can my character wear a blue shirt? ^start(animations/Stand/Gestures/Hey_3)",
     "\\vct=100\\I'm excited! Let's play! ^start(animations/Stand/Gestures/Hey_4)"
    ],
    # Robot B lines
    ["\\vct=0\\Do you want to play a videogame? ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=0\\It will be fun. Do you want to play? ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=0\\You get to make your own character! ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=0\\What do you think? ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=0\\It is a game with characters that make facial expressions. ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=0\\You can play on your computer. ^start(animations/Stand/Gestures/Hey_2)",
     "\\vct=0\\Yes! Are you ready to play? ^start(animations/Stand/Gestures/Hey_2)"
    ]
]

espexVocab = [
    [['video', 'game'],
     ['to', 'play'],
     ['own', 'character'],
     ['you', 'think'],
     ['facial', 'expressions'],
     ['your', 'computer'],
     ['to', 'play']
    ],
    [['is', 'it'],
     ['i', 'play'],
     ['blue', 'shirt'],
     ['excited', 'play']
    ]
]
