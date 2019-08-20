"""
基于fork的进程创建演示2
"""
import os
pid=os.fork()
print("----------------------------------")
a=1
while True:
    if pid<0:
        print("Create process failed")
    elif pid==0:
        print("new process")
        print(a)
        a=1000
    else:
        print("Old process")
        print(a)
    print("a:",a)