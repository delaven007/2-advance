"""
epoll服务端程序

尽量掌握

思路分析：
【1】 创建套接字
【2】 将套接字register
【3】 创建查找字典，并维护(与注册的io保持一致)
【4】 循环监控IO发生
【5】 处理发生的IO
"""
from socket import *
from select import *

s=socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("localhost", 6060))
s.listen(1)
#创建epoll对象关注s
ep=epoll()
#建立查找字典，用于通过fileno查找io对象
fdmap={s.fileno():s}
#关注s
ep.register(s,EPOLLIN | EPOLLERR)

#循环监控
while True:
    events=ep.poll()
    #循环遍历发生事件        fd-->fileno
    for fd,event in events:
        #区分时间进行处理
        if fd==s.fileno():
            c,addr=fdmap[fd].accept()
            print("Connect from",addr)
            #添加新的关注io
            #添加一个监控对象，就添加一个io事件
            ep.register(c, EPOLLIN | EPOLLERR)
            fdmap[c.fileno()]=c    #维护字典
            #按位与判定POLLIN就绪
        elif event & EPOLLIN:
            data=fdmap[fd].recv(4096).decode()
            if not data:
                ep.unregister(fd)      #取消关注
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print("Receive:",data.encode())
            fdmap[fd].send("OK".encode())





