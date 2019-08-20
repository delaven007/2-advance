"""
2.0
io多路复用
思路分析
1.实用类封装
2.在用户使用角度，决定类的编写

"""
from socket import *
from select import *


# 封装类 http server 功能
class HTTPServer:
    def __init__(self, host, port, dir):
        self.address = (host, PORT)
        self.host = host
        self.port = port
        self.dir = dir

        self.rlist = []
        self.wlist = []
        self.xlist = []

        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    #
    def bind(self):
        self.sockfd.bind(self.address)

    #启动服务
    def serve_forver(self):
        self.sockfd.listen(1)
        print("Listen the port %d" % self.port)
        self.rlist.append(self.sockfd)
        while True:
            rs,ws,xs=select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c,addr=r.accept()
                    print("Connect from:%d",addr)
                    self.rlist.append(c)
                else:
                    #处理请求
                    self.handle(r)

    # 具体处理请求
    def handle(self, connfd):
        # 接受客户端HTTP请求
        requst = connfd.recv(4096)
        # print(requst)
        if not requst:
            self.rlist.remove(connfd)
            connfd.close()
            return
        # 提取请求内容
        requst_line = requst.splitlines()[0]
        info = requst_line.decode().split(" ")[1]
        print(connfd.getpeername(), ":", info)

        if info =="/" or info[-5:]==".html":
            self.get_html(connfd,info)

        else:
            pass
    def get_html(self,connfd,info):
        if info=="/":
            filename=self.dir+"/index.html"
        else:
            filename=self.dir+info
        try:
            fd= open(filename)
        except Exception:
            #无网页
            responseHeaders="http/1.1 404 Not Found\r\n"
            responseHeaders+="\r\n"
            responseBody="Sorry,not found the page"
        else:
            responseHeaders = "http/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
            responseBody = fd.read()
        finally:
            response=responseHeaders+responseBody
            connfd.send(response.encode())
    def get_data(self,connfd,info):
        responseHeaders = "http/1.1 200 OK\r\n"
        responseHeaders += "\r\n"
        responseBody = "Waiting for httpserver 3.0"
        response = responseHeaders + responseBody
        connfd.send(response.encode())


if __name__ == "__main__":
    """
    希望通过HTTPSERVER类快速搭建HTTP服务
    展示网页
    """
    # 用户自己决定
    HOST = ("127.0.0.1")
    PORT = 8080
    DIR = "./static"  # 网页存储路径

    httpd = HTTPServer(HOST, PORT, DIR)  # 实例化对象
    httpd.serve_forver()  # 启动HTTP服务
