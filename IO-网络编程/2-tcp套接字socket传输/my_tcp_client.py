from socket import *
import time
sockfd = socket()
server_addr = (("127.0.0.1",6666))
sockfd.connect(server_addr)

fd = open("exe", "rb")
sockfd.send(fd.name.encode())
data=sockfd.recv(1024).decode()
print(data)
n=fd.read()
# time.sleep(0.00001)
sockfd.send(n)
data=sockfd.recv(4096).decode()
print(data)
fd.close()
sockfd.close()

