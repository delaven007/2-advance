from socket import *
import os
import sys
ADDR=("localhost",9999)

def send_msg(s,name):
    while True:
        try:
            text=input("say:")
        except KeyboardInterrupt:
            text="quit"
        if text.strip()=="quit":
            msg="Q"+name
            s.sendto(msg.encode(),ADDR)
            sys.exit("退出聊天室")
        msg="C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)

def recv_msg(s):
    while True:
        try:
            data,addr=s.recvfrom(4096)
        except KeyboardInterrupt:
            sys.exit()
        if data.decode()=="exit":
            sys.exit()
        print(data.decode()+"\n发言：",end=" ")

def main():
    s=socket(AF_INET,SOCK_DGRAM)
    while True:
        name=input("姓名：")
        msg="L "+name
        s.sendto(msg.encode(),ADDR)
        data,addr=s.recvfrom(4096)
        if data.decode()=="OK":
            print("您已进入聊天室")
            break
        else:
            print(data.decode())

    pid=os.fork()
    if pid<0:
        sys.exit("Error")
    elif pid==0:
        send_msg(s,name)
    else:
        recv_msg(s)
if __name__=="__main__":
    main()
