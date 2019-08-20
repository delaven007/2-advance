"""
创建套接字
设置套接字可以接受广播
选择接收端口
"""
from socket import *

s = socket(AF_INET, SOCK_DGRAM)

# 让套接字接受广播
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.bind(("0.0.0.0", 6666))

while True:
    msg, addr = s.recvfrom(8192)
    print(msg.decode())

s.close()
