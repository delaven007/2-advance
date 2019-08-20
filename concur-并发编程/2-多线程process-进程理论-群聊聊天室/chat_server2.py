from socket import *
import os,sys
ADDR=("localhost",9999)
user={}
def do_login(s,name,addr):
    if name in user or "管理员" in name:
        s.sendto("该用户已存在".encode(),addr)
        return
    s.sendto("OK".encode(),addr)
    msg="欢迎 %s 进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name]=addr
def do_chat(s,name,text):
    msg="%s:%s"%(name,text)
    for i in user:
        if i !=name:
            s.sendto(msg.encode(),user[i])
def do_quit(s,name):
    msg="%s 退出聊天室"%name
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto("text".encode(),user[i])
    del user[name]
def do_request(s):
    while True:
        data,addr=s.recvfrom(4096)
        tmp=data.decode().split(" ")
        if tmp[0]=="L":
            do_login(s,tmp[1],addr)
        if tmp[0]=="C":
            text=" ".join(tmp[2:])
            do_chat(s,tmp[1],text)
        elif tmp=="Q":
            if tmp[1] not in user:
                s.sendto("exit".encode(),addr)
                continue
            do_quit(s,tmp[1])
def main():
    s=socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    pid=os.fork()
    if pid<0:
        return
    elif pid==0:
        while True:
            msg=input("管理员消息：")
            msg="C 管理员消息" +msg
            s.sendto(msg.encode(),ADDR)
            do_request(s)
    else:
        do_request(s)
if __name__=="__main__":
    main()
