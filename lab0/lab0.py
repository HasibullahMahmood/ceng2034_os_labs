
import os
import time
from datetime import datetime

os.chdir(os.environ.get('HOME'))
os.system('mkdir os_lab_0')
os.chdir('os_lab_0')
os.system("touch 1.txt 2.txt 3.py")

for item in os.listdir():
    if os.path.isfile(item):
        print("last modified: ", time.ctime(os.path.getmtime(item)), item)

for item in os.listdir():
    if os.path.isfile(item) and item.endswith(".txt"):
        print(item)
