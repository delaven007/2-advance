"""
线程属性
"""

from threading import Thread
from time import sleep
def fun():
    sleep(3)
    print("线程属性测试")

t=Thread(target=fun,name="tude")
#主线程退出，分支线程也退出
t.setDaemon(True)
print("name:",t.getName())
print("alive:",t.is_alive())
t.start()
t.setName("tarena")
print("name:",t.getName())     #线程名称
print("alive:",t.is_alive())      #线程生命周期
print("daemon:",t.isDaemon())

# t.join()



