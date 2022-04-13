# PowerShell script for windows that runs two background python processes--
# one for each robot
# Execute multiple NAO robot python scripts
# Running this script requires: `Set-ExecutionPolicy RemoteSigned` (need admin privileges)
# Hack for getting around this: open the script in PowerShell ISE and run it
# (It might need to be copy-pasted into an untitled script to work)

# Replace ips with NAO robot ips
$ip1="192.168.208.108"
$ip2="192.168.208.73"
$port1=9558
$port2=9559

C:\Python27\pythonw.exe test.py --ip $ip1 --port $port1
C:\Python27\pythonw.exe test.py --ip $ip2 --port $port2
