import socket
import os
import sys
import pickle

def getSavedObj():
	try:
		f = open(os.path.join(os.environ['tmp'],'autoclick.conf'),'rb')
		savedObj = pickle.load(f)
		f.close()
		return savedObj
	except FileNotFoundError:
		return None
	
def saveObj(obj):
	f = open(os.path.join(os.environ['tmp'],'autoclick.conf'),'wb')
	pickle.dump(obj, f)
	f.close()

def getArgList(arg):
	list = arg.split('.')
	list = [l for l in list if len(l) > 0 and l.isdigit() and int(l) > -1 and int(l) < 256]
	return list
	
savedIp = getSavedObj()

newIpList = []
for i in range( len(sys.argv) -1 ):
	newIpList += getArgList(sys.argv[i+1])
	
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
saveObj(finalIp)

cmd = "adb connect " + finalIp  + ":6666"
print(cmd)
os.system(cmd)
os.system("adb devices")