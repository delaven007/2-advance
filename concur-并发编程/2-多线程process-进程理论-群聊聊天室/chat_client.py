"""
客户端
1.输入姓名
2.将姓名发送给服务器
3.收到服务器反馈
4.进入聊天室或重新输入

1.创建新的进程
2.父进程收消息
3.子进程发消息

1.发送退出请求
2.结束进程，发送进程
3.接受exit表示接受
"""
import os
import sys
from socket import *
#服务端地址
ADDR=("localhost",6666)

#发送消息
def send_msg(s,name):
    while True:
        try:
            text=input("say:")
        except KeyboardInterrupt:
            text="quit"
        #退出
        if text.strip()=="quit":
            msg="Q" + name
            s.sendto(msg.encode(),ADDR)
            sys.exit("退出聊天室")
        msg="C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)

#接收消息
def recv_msg(s):
    while True:
        try:
            data,addr=s.recvfrom(4096)
        except KeyboardInterrupt:
            sys.exit()
        #服务器发送RXIt退出
        if data.decode()=="exit":
            sys.exit()
        print(data.decode()+"\n发言：",end=" ")

#启动客户端
def main():
    s=socket(AF_INET,SOCK_DGRAM)
    while True:
        name=input("姓名：")
        msg="L " + name
        s.sendto(msg.encode(),ADDR)
        #等待反馈
        data,addr=s.recvfrom(4096)
        if data.decode()=="OK":
            print("您已进入聊天室")
            break
        else:
            print(data.decode())
    #创建新的进程
    pid=os.fork()
    if pid<0:
        sys.exit("Error")
    elif pid==0:
        send_msg(s,name)
    else:
        recv_msg(s)

if __name__=="__main__":
    main()