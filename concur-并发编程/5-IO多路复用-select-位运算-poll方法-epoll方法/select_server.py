"""
tcp服务模型

*重点*

思路：
【1】 将关注的IO放入对应的监控类别列表
【2】通过select函数进行监控
【3】遍历select返回值列表，确定就绪IO事件
【4】处理发生的IO事件
"""
from socket import *
from select import select

# 创建监听套接字作为关注 io
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("localhost", 6060))
s.listen(1)

#设置关注列表
rlist=[s]
wlist=[]
xlist=[]

while True:
    #监控io
    rs,ws,xs=select(rlist,wlist,xlist)
    #遍历三个返回列表，处理io
    for r in rs:
        #根据遍历到io的不同用if分情况处理
        if r is s:
            c,addr=r.accept()
            print("Connect from",addr)
            rlist.append(c)          #增加新的io事件

        else:
            data=r.recv(4096)
            
            #客户端退出
            if not data:
                rlist.remove(r)  #从关注列表移除
                r.close()
                continue        #继续处理其他io
            print("Receive:",data.decode())
            # r.send("OK".encode())
            #主动处理io对象
            wlist.append(r)
    for w in ws:
        w.send("OK".encode())
        wlist.remove(w)      #使用后移除

        pass
    for x in xs:
        pass
