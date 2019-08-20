"""
1.将一个文件，从客户端发送到服务端，文件类型随意
读取--》send
接受--》write
2.tcp程序，函数
"""
#1.
from socket import *
sockfd=socket()
server_addr=("127.0.0.1",6666)             #服务端地址
sockfd.connect(server_addr)

filename=input("file_name：")
try:
    f=open(filename,"r+")

except FileNotFoundError as e:
    print(e)



else:
    fw=open("file","wb")
    while  True:
        data=f.read(2048)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()