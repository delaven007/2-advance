"""
线程使用
"""
from  threading import Thread
# import threading
from time import sleep
import os
a=1
#创建线程函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放黄河大合唱")
        global a
        print("a=",a)
        a=1000
#创建线程对象
t=Thread(target=music)
t.start()              #启动

for i in range(4):
    sleep(1)
    print(os.getpid(), "播放三天三夜")
    print("main a:",a)
t.join()               #回收