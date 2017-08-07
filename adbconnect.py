import socket
import os
import sys
import pickle
import re

def getSavedObj():
	try:
		f = open(os.path.join(os.environ['tmp'],'adbconnect.conf'),'rb')
		savedObj = pickle.load(f)
		f.close()
		return savedObj
	except FileNotFoundError:
		return None
	
def saveObj(obj):
	f = open(os.path.join(os.environ['tmp'],'adbconnect.conf'),'wb')
	pickle.dump(obj, f)
	f.close()

def getArgList(arg):
	list = arg.split('.')
	list = [l for l in list if len(l) > 0 and l.isdigit() and int(l) > -1 and int(l) < 256]
	return list
	
ipDict = getSavedObj()
if ipDict == None:
	ipDict = dict()
#print("dict",ipDict)
savedIp = None
savedPort = None
savedName = "default"

if len(sys.argv) > 1 and not sys.argv[1].split('.')[0].isdigit():
	savedName = sys.argv[1]

#print("savedName", savedName)
savedIp = ipDict.get(savedName,(None, None))[0]
savedPort = ipDict.get(savedName,(None, None))[1]

#print("savedIp", savedIp)
#print("savedPort", savedPort)

reg_port = re.compile(r'.*:(.*)')
newPort = None

for i in range( len(sys.argv) -1 ):
	if newPort == None:
		reg_res = reg_port.search(sys.argv[i+1])
		if reg_res:
			newPort = reg_res.groups()[0]
			sys.argv[i+1] = sys.argv[i+1].split(":")[0]

newIpList = []
for i in range( len(sys.argv) -1 ):
	newIpList += getArgList(sys.argv[i+1])
			

#print("new port", newPort)
if newPort == None:
	if savedPort == None:
		print("无缓存Port，需要重新输入")
		exit()
	newPort = savedPort

newIpLen = len(newIpList)

if savedIp == None and newIpLen < 4:
	print('当前无缓存数据，请输入完整Ip')
	exit()

usableIpInSaved = 4 - newIpLen
if savedIp == None:
	savedList = []
else:
	savedList = savedIp.split('.')[:usableIpInSaved]
finalIpList =  savedList + newIpList

finalIp = '.'.join(finalIpList)
#print("newIp",finalIp)

ipDict[savedName] = (finalIp, newPort)
ipDict["default"] = ipDict[savedName]
#print("beforeSave",ipDict)
saveObj(ipDict)

cmd = "adb connect " + finalIp  + ":" + newPort
print(cmd)
os.system(cmd)
os.system("adb devices")