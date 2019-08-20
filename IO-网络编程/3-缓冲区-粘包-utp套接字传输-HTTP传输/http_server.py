"""
发送网页给浏览器
"""
from socket import *
#处理客户端请求
def handle(connfd):
    request=connfd.recv(4096)
    #防止客户端断开
    if not request:
        return
    request_line=request.splitlines()[0]
    info=request_line.decode().split(" ")[1]
    if info =="/":
        with open("index.html") as f:
            response="http/1.1 200 OK\r\n"
            response+="Content-Type:text/html\r\n"
            response+="\r\n"
            response+=f.read()
    else:
        response = "http/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Sorry，您浏览的页面已丢失</h1>"
    #发送给浏览器
    connfd.send(response.encode())
#搭建tcp网络
sockfd=socket()
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
sockfd.bind(("localhost",9000))
sockfd.listen(4)
while True:
    connfd,addr=sockfd.accept()
    handle(connfd)   #处理客户端请求

