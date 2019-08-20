"""
进程对象属性
"""
from multiprocessing import Process
from time import sleep,ctime
def tm():
    for i in range(3):
        sleep(2)
        print(ctime())
p=Process(target=tm)  #,name="..."
# p.daemon=True        #子进程会随父进程退出
p.start()
print("name:",p.name)
print("PID:",p.pid)
print("IS_alive:",p.is_alive())
