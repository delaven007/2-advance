"""
multiprocessing2
"""
from multiprocessing import Process
from time import sleep
import os

def th1():
    sleep(5)
    print("写")
    print(os.getppid(),"----",os.getpid())

def th2():
    sleep(5)
    print("测")
    print(os.getppid(),"----",os.getpid())

def th3():
    sleep(5)
    print("发")
    print(os.getppid(),"----",os.getpid())

things = [th1,th2,th3]
jobs = []
for th in things:
    p=Process(target=th)
    p.start()
    # p.join()
    jobs.append(p)        #将进程对象保存到列表里
for i in jobs:
    i.join()



