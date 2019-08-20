"""
练习：线程类
可以让player作为线程运行
player只是测试函数，名称和参数均不确定

"""
from threading import Thread
from time import sleep,ctime
class MyThread(Thread):
    def __init__(self,target=None,args=(),kwargs=dict({})):
        super().__init__()
        self.target=target
        self.args=args
        self.kwargs=kwargs
    def run(self):
        self.target(*self.args,**self.kwargs)

def player(sec,song):
    for i in range(3):
        print("Playing %s : %s"%(song,ctime()))
        sleep(sec)

t=MyThread(target=player,args=(3,),kwargs={"song":"凉凉"})
t.start()
t.join()
