"""
套接字非阻塞

如果没有客户端连接。每隔三秒填充一个日志
"""
from socket import *
from time import sleep,ctime

f=open("log.txt","a+")
#创建tcp套接字
sockfd=socket()
sockfd.bind(("localhost",1212))
sockfd.listen(1)

#设置套接字为非阻塞
# sockfd.setblocking(False)
sockfd.settimeout(2)

while True:
    print("等待连接...")
    try:
        connfd,addr=sockfd.accept()
    except (BlockingIOError,timeout) as e:
        #如果没有客户端连接，每隔三秒写一个日志
        f.write("%s:%s\n"%(ctime(),e))
        f.flush()
        sleep(1)
    else:
        print("connect from",addr)
        data=connfd.recv(4096).decode()
        print(data)





