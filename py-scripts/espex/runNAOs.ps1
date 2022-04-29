$ipA='169.254.75.247'
$portA=9559
$fileA="data/dataA.csv"

$ipB='169.254.15.57'
$portB=9559
$fileB="data/dataB.csv"
$mode='espex'

# python2.7 test.py $ipA $portA $fileA $mode
C:\Python27\pythonw.exe statemachineA.py $ipA $portA $fileA $mode
sleep 3
C:\Python27\python.exe statemachineB.py $ipB $portB $fileB $mode
#python3 processData.py $fileA $fileB $t
