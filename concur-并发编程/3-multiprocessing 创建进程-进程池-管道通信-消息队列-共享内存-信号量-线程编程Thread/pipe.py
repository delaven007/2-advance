"""
管道通道
"""
from multiprocessing import Process, Pipe
import os, time

# 创建管道对象  False  fd1只能recv   fd2只能send
fd1, fd2 = Pipe(False)


def write():
    while True:
        # time.sleep()
        fd2.send(time.ctime())  # 向管道发送内容


def read():
    while True:
        data = fd1.recv()  # 从管道获取消息
        print(data)


r = Process(target=read)
w = Process(target=write)
r.start()
w.start()
r.join()
w.join()
