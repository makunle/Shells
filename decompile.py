import sys
import os
import winreg

tools_path = r'D:\Software\DecompileTools'

apktool_dir = 'apktool'
dex2jar_dir = 'dex2jar-2.0'
jdjui_dir = 'jd-gui'

jar_file_path = None

def run():
	k,*v = input("[.apk -> apktool, .dex -> dex2jar, .jar -> jdjui] > ").split(' ')
	if k == 'apktool':
		perform_apktool(v)
	elif k == 'dex2jar':
		perform_dex2jar(v)
	elif k == 'jdjui':
		perform_jdjui(v)
	elif k == 'exit':
		exit()
	elif len(k) > 0:
		if k.endswith('.apk'):
			perform_apktool([k] + v)
		elif k.endswith('.dex'):
			perform_dex2jar([k] + v)
		elif k.endswith('.jar'):
			perform_jdjui([k] + v)
	else:
		print(k)
		print(v)
		os.system(k + ' ' + ' '.join(v))

def perform_apktool(v):
	cmd = 'start ' + tools_path + '\\' + apktool_dir
	arg = '\\apktool d ' + ' '.join(v) + ' -f -o ' + v[0].split('.')[0]
	print(cmd + arg)
	os.system(cmd + arg)

def perform_dex2jar(v):
	global jar_file_path
	cmd = 'start ' + tools_path + '\\' + dex2jar_dir + '\\d2j-dex2jar ' + ' '.join(v)
	filepath = v[0].split('.')[0] + '-dex2jar.jar'
	jar_file_path = filepath
	cmd += ' -f -o ' + filepath
	print(cmd)
	os.system(cmd)

def perform_jdjui(v):
	global jar_file_path
	cmd = 'java -jar ' + tools_path + '\\' + jdjui_dir + '\\jd-gui-1.4.0.jar '
	argv = ""
	if len(v) > 0:
		argv = ' '.join(v)
	elif jar_file_path != None:
		argv = '"' + jar_file_path + '"'
	print(cmd + argv)
	os.system(cmd + argv)

if __name__ == '__main__':
	while True:
		run()
	
