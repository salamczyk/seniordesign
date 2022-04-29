#!/bin/bash

t=$(date +%s)

ipA='169.254.75.247'
portA=9559
fileA="data/dataA$t.csv"

ipB='169.254.15.57'
portB=9559
fileB="data/dataB$t.csv"
mode='espex'

# python2.7 test.py $ipA $portA $fileA $mode
python2.7 statemachineA.py $ipA $portA $fileA $mode &
sleep 3
python2.7 statemachineB.py $ipB $portB $fileB $mode
python3 processData.py $fileA $fileB $t
