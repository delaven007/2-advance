from socket import *

sockfd=socket(AF_INET,SOCK_DGRAM)
s_addr=("localhost",6666)
sockfd.connect(s_addr)

while True:
    data=input(">>")
    if not data:
        break
    m=sockfd.sendto(data.encode(),s_addr)
    print("发送%d Btys"%m)
    msg,s_addr=sockfd.recvfrom(4096)
    print(msg.decode())
sockfd.close()