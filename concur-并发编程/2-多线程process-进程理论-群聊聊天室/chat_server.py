"""
chat room
encv:python 3.6
socket udp fork
1.收到请求
2.判断姓名是否存在
3.反馈信息给客户
4.不允许进入结束，允许进入将用户插入字典
5.通知其他用户

1.接受请求
2.将消息转发给其他人
"""

from socket import *
import os,sys
#服务器地址
ADDR=("localhost",6666)
#存储用户字典{name,addr}
user={}

#登录
def do_login(s,name,addr):
    if name in user or "管理员" in name:
        s.sendto("该用户已存在".encode(),addr)
        return
    s.sendto("OK".encode(),addr)
    #通知其他
    msg="欢迎 %s 进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    #插入字典
    user[name]=addr

#向其他用户发消息
def do_chat(s,name,text):
    msg="%s:%s"%(name,text)
    for i in user:
        if i !=name:
            s.sendto(msg.encode(),user[i])

#退出
def do_quit(s,name):
    msg="%s 退出聊天室"%name
    for i in user:
        if i !=name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto("text".encode(),user[i])
    #从字典删除
    del user[name]

#循环接受客户端的请求
def do_request(s):
    while True:
        data,addr=s.recvfrom(4096)
        tmp=data.decode().split(" ")   #拆分请求
        #根据请求类型，执行不同内容
        if tmp[0]=="L":
            do_login(s,tmp[1],addr)
        if tmp[0]=="C":
            text=" ".join(tmp[2:])     #拼接消息内容
            do_chat(s,tmp[1],text)     #完成客户端登录进入工作
        elif tmp=="Q":
            if tmp[1] not in user:
                s.sendto("exit".encode(),addr)
                continue
            do_quit(s,tmp[1])
#搭建udp网络
def main():
    #udp套接字
    s=socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    pid=os.fork()
    if pid<0:
        return
    elif pid ==0:
        while True:
            msg=input("管理员消息：")
            msg="C 管理员消息 "+msg
            s.sendto(msg.encode(),ADDR)
            do_request(s)

    else:
        # 请求处理函数
        do_request(s)

if __name__=="__main__":
    main()


