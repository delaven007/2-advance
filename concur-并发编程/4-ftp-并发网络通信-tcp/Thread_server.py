"""
基本与进程相同，只是换为线程请求
档主线程结束，同时终止所有客户端请求
"""

from threading import Thread
from socket import *
import sys
# import signal

HOST ="localhost"
POST=6666
ADDR=(HOST,POST)

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(1)

# signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("监听端口%d...."%POST)

def handle(c):
    while True:
        data=c.recv(4096)
        if not data:
            break
        print(data.decode())
        c.send("OK".encode())
    c.close()

while True:
    try:
        c,addr=s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue

    t=Thread(target=handle,args=(c,))
    t.setDaemon(True)          #设置主线程退出，子进程也退出
    t.start()


    # if t==0:
    #     s.close()
    #     handle(c)
    #     sys.exit(0)
    # c.close()
