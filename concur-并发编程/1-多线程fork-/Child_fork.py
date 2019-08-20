"""
二级子进程处理僵尸
"""
import os
from time import sleep

def f1():
    for i in range(5):
        sleep(2)
        print("写代码")
def f2():
    for i in range(5):
        sleep(2)
        print("工作")

pid=os.fork()
if pid <0:
    print("Error")
elif pid==0:
    p=os.fork()    #二级子进程
    if p ==0:
        f2()
    else:
        os._exit(0)            #一级子进程
else:
    os.wait() #等一级子进程退出
    f1()
