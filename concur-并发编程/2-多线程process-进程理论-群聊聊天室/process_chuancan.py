# from multiprocessing import Process
# from time import sleep
#
# #带参数的进程函数
# def worker(sec,name):
#     for i in range(3):
#         sleep(sec)
#         print("I'm %s "%name)
#         print("I'm working...")
#
# p=Process(target=worker,kwargs={"name":"Delaven","sec":5})
# # p=Process(target=worker,args=(2,),kwargs={"name":"Bar"})
# p.start()
# p.join()

from multiprocessing import Process
from time import sleep
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("hello")
        print("world")
        print(name)
# p=Process(target=worker,kwargs={"name":"Delaven","sec":5})
p=Process(target=worker,args=(2,),kwargs={"name":"Dog"})
p.start()
p.join()