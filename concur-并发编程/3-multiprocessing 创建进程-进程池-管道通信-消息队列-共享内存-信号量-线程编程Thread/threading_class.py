"""
自定义线程类
"""
from threading import Thread
"""
1.继承Thread
2.重写__init__ 和 run
"""
class ThreadClass(Thread):
    def __init__(self,attr):
        self.attr=attr
        super().__init__()

    #很多方法一起完成任务
    def f1(self):
        print("1")
    def f2(self):
        print("2")

    def run(self):
        self.f1()
        self.f2()
t=ThreadClass("XXXX")
t.start()
t.join()