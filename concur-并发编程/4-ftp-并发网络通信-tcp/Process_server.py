"""
多进程并发
"""

from socket import *
import sys
import signal
import multiprocessing as mp

HOST ="localhost"
POST=6666
ADDR=(HOST,POST)

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(1)

signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("监听端口%d...."%POST)

def handle(c):
    while True:
        data=c.recv(4096)
        if not data:
            break
        print(data.decode())
        c.send("OK".encode())
    c.close()
    s.close()
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue

    p=mp.Process(target = handle,args=(c,))
    p.start()        #启动进程
    p.daemon=True
    # sys.exit(0)
