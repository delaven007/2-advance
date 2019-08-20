"""
基于fork的进程创建演示
"""
import os
from time  import sleep
pid=os.fork()
while True:
    if pid<0:
        print("Create process failed")
    elif pid==0:
        sleep(3)
        print("new process")
    else:
        sleep(5)
        print("Old process")

    print("Fork test end")