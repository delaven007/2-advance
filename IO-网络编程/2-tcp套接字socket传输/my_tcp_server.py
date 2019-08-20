"""
服务端
"""
import socket
import time
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockfd.bind(("127.0.0.1",6666))
sockfd.listen(2048)

while True:
    print("等待连接......")
    try:
        connfd, addr = sockfd.accept()
        print("连接在", addr)
    except KeyboardInterrupt:
        print("退出")
        break

    data_name=connfd.recv(4096).decode()
    file_size=connfd.send("*已接收文件名字*".encode())
    print("发送了%d Btys" % file_size)
    fd = open(data_name+"1", "wb")
    # time.sleep(0.00001)
    data = connfd.recv(10)
    file_size = connfd.send("*已接收文件内容*".encode())
    # time.sleep(0.00001)
    print("发送了%d Btys" % file_size)
    fd.write(data)
    fd.close()
    connfd.close()
sockfd.close()
