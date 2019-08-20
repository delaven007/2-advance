"""
tcp客户端流程
***
"""
from socket import *
#创建tcp流式套接字
sockfd=socket()                     #参数默认即为tcp套接字
#连接服务端程序
server_addr=("127.0.0.1",6061)             #服务端地址
sockfd.connect(server_addr)
#消息发送
while True:
    data=input("msg>>>")
    #设置循环结束条件：直接回车
    if not data:
        break
    sockfd.send(data.encode())         #转换字节串
    data=sockfd.recv(2048)
    print("server:",data.decode())
sockfd.close()





