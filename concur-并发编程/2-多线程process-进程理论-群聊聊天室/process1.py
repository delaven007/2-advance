"""
multiprocessing

"""
import os
import multiprocessing as mp
from time import sleep

a = 1
def fun():
    print("开始一个新的进程")
    sleep(10)
    global a
    print(a)
    a=10000
    print("子进程结束")
#创建进程对象
p=mp.Process(target = fun)
p.start()        #启动进程
sleep(5)
print("父进程干活")
p.join(1)         #回收进程
print(a)
#等价：
# pid=os.fork()
# if pid==0:
#     fun()
# elif pid>0:
#     os.wait()
