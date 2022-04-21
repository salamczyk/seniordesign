#!/bin/bash

t=$(date +%s)

ipA='192.168.208.177'
portA=9559
fileA="dataA$t.csv"

ipB='192.168.208.231'
portB=9559
fileB="dataB$t.csv"

python2.7 statemachineA.py $ipA $portA $fileA &
sleep 3
python2.7 statemachineB.py $ipB $portB $fileB
python3 processData.py $fileA $fileB $t
