
from socket import *
#创建套接字
socketfd=socket(AF_INET,SOCK_DGRAM)
#绑定地址
server_addr=(("localhost",6666))
socketfd.bind(server_addr)

#收发消息
while True:
    data,addr=socketfd.recvfrom(8192)
    if not data:
        break
    print(data.decode())
    n=socketfd.sendto("receive".encode(),addr)
#关闭套接字
socketfd.close()