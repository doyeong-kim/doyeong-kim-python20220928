# demoRandom.py

from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES
import random

print(random.random())
print(random.random())

lotto = list(range(1,46))
print(lotto)
random.shuffle(lotto)

print(lotto)

print("---샘플링----")
print(random.sample(range(20),10))
print(random.sample(range(20),10))
print(random.sample(range(20),10))

#파일명 다루기
from os.path import *
print( abspath("python.exe"))
print( basename("c:\\Python39\\python.exe"))
print( getsize("c:\\Python38\\python.exe"))

#운영체제 정보 
from os import *
print("운영체제 : ", name)
#system("notepad.exe")

#파일리스트
import glob
print( glob.glob("c:\\work\\*.py"))