import socket
import os
import sys

hostname = socket.gethostname()
myip = socket.gethostbyname(hostname)

deviceip = sys.argv[1]
lens = len(deviceip.split('.'))
need = 4 - lens
dstip = '.'.join(myip.split('.')[:need]) + '.' + deviceip
cmd = "adb connect " + dstip  + ":6666"
print(cmd)
os.system(cmd)
os.system("adb devices")