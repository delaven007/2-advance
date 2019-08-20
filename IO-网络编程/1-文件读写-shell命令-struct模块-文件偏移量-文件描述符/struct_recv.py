"""
思路
创建套接字
循环接收内容
将接受内容写入文件
"""
from socket import *
import struct
#创建套接字
#udp
socketfd=socket(AF_INET,SOCK_DGRAM)
#绑定地址
server_addr=(("localhost",6666))
socketfd.bind(server_addr)
#数据结构
st=struct.Struct("i32sif")
#打开文件
f=open("student.txt","a")
#收发消息
while True:
    data,addr=socketfd.recvfrom(8192)
    data=st.unpack(data)        #解析数据
    #整理数据
    info="%d %-10s %d %.1f\n"%\
         (data[0],data[1].decode(),data[2],data[3])
    f.write(info)
    f.flush()
f.close()
socketfd.close()
