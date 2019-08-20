"""
套接字属性
"""
from socket import *

#创建套接字
s=socket()
#设置套接字端口立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(("127.0.0.1",6666))
s.listen(3)
c,addr=s.accept()

c.recv(3)
print("地址类型",s.family)
print("套接字绑定地址",s.getsockname())
print("套接字类型",s.type)
print("套接字的文件描述符",s.fileno())
print("获取连接客户端的地址",c.getpeername())
print("获取选项值",s.getsockopt(SOL_SOCKET,SO_REUSEADDR))