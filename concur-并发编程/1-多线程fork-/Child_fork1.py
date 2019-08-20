import os
from time import sleep

def fun1():
    for i in range(6):
        sleep(1)
        print("fun1")
def fun2():
    for i in range(5):
        sleep(1)
        print("fun2")
fd=os.fork()
if fd <0:
    print("Error")
elif fd==0:
    f=os.fork()
    if f==0:
        fun2()
    else:
        os._exit(0)
else:
    os.wait()
    fun1()