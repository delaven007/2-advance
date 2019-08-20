"""
消息队列演示
"""
from multiprocessing import Process, Queue
from time import sleep
from random import randint

#  创建消息队列
q = Queue(3)
#请求进程
def request():
    for i in range(10):
        x=randint(0,100)
        y=randint(0,100)
        q.put((x,y))

#处理进程
def handle():
    while True:
       sleep(0.0001)
       try:
           x,y=q.get(timeout=3)
       except:
           break
       else:
           print("%d + %d =%d"%(x,y,x+y))

p1=Process(target=request)
p2=Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()