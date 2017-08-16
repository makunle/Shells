import socket
import os
import sys
import pickle
import re

args = ' '.join(sys.argv[1:])
os.system("python adbconnect.py " + args)