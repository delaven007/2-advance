"""
基于协程tcp并发
"""
#处理客户端请求
def handle(c):
    while True:
        data=c.recv(4096)
        if not data:
            break
        print(data.decode())
        c.send("OK".encode())
    c.close()
import gevent
from gevent import monkey
monkey.patch_all()           #在导入socket前执行
from socket import *

fd=socket()
fd.bind(("localhost",6061))
fd.listen(1)
while True:
    #等待连接
    print("Wait Connect...")
    c,addr =fd.accept()
    print("Connect from",addr)
    # handle(c)
    gevent.spawn(handle,c)
fd.close()