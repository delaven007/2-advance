import socket
socketfd=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

socketfd_addr=("172.40.74.177",22222)
socketfd.connect((socketfd_addr))

while True:
    data=input("word>>")
    if not data:
        break
    m=socketfd.sendto(data.encode(),socketfd_addr)
    print("接受了%d Btys"%m)
    msg,socketfd_addr=socketfd.recvfrom(4096)
    print(msg.decode())

socketfd.close()
