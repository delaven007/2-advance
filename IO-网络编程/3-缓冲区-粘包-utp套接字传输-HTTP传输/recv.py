from  socket import *

sockfd=socket(AF_INET,SOCK_DGRAM)
fd_addr=("127.0.0.1",6666)
sockfd.bind(fd_addr)
while True:
    data,fd_addr=sockfd.recvfrom(8192)
    if not data:
        break
    print(data.decode())
    m=sockfd.sendto("receive".encode(),fd_addr)
    print("接收%d Btys"%m)

sockfd.close()