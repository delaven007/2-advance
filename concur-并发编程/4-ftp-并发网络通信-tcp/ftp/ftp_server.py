"""
ftp文件服务器分析
1.技术分析
    *并发模型   多线程并发
    *网络       tcp传输

2.结构设计
    *客户端发起请求-->界面
    list    get filename    put   filename

    *服务端 用类封装
3.功能模块
    *网络并发结构
    1.查看文件类型
    2.下载文件
    3.上传文件
    *退出
4.协议设定
    *文件列表查看：普通文件（非隐藏）
    *客户端请求类型：L  文件列表
                  G  filename    下载
                  P filename   上传
                  Q    退出
"""
"""
ftp文件服务器
多线程并发/线程练习
"""
from threading import Thread
import os
from socket import *
import time

#全局变量
HOST="localhost"
PORT=9898
ADDR=(HOST,PORT)
ftp="/home/tarena/ftp/"      #文件库位置

#创建文件服务器服务端功能类
class FTPServer(Thread):
    def __init__(self,connfd):
        self.connfd=connfd
        super().__init__()

    # 获取文件列表
    def do_list(self):

        files=os.listdir(ftp)
        if not files:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send("OK".encode())
            time.sleep(0.01)         #防止和后面内容发生粘包
        #拼接文件列表
        files_=""
        for file in files:
            #非隐藏文件和不是普通文件
            if file[0] !="."and os.path.isfile(ftp+file):
                files_ += file+"\n"
        self.connfd.send(files_.encode())
    #下载
    def do_get(self,filename):
        try:
            fd=open(ftp+filename,"rb")
        except Exception:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send("OK".encode())
            time.sleep(0.1)
        #文件发送
        while True:
            data=fd.read(4096)
            if not data:
                time.sleep(0.01)
                self.connfd.send("##".encode())
                break
            self.connfd.send(data)
    #上传文件
    def do_put(self,filename):
        fd=open(ftp+filename,"wb")
        while True:
            data=self.connfd.recv(4096)
            if data==b"##":
                break
            fd.write(data)
        fd.close()


    #循环接受客户端请求
    def run(self):
        while True:
            data=self.connfd.recv(4096).decode()
            if not data or data =="Q":
                return
            elif data=="L":
                self.do_list()
            elif data[0]=="G":         #G filename
                filname=data.split(" ")[-1]
                self.do_get(filname)
            elif data[0]=="P":         #P filename
                filname=data.split(" ")[-1]
                self.do_put(filname)

def main():
    sockfd=socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(1)
    print("监听端口%d....", PORT)

    while True:
        try:
            connfd,addr=sockfd.accept()
        except KeyboardInterrupt:
            print("服务期退出")
            return
        except Exception as e:
            print(e)
            continue
    #创建新的线程处理客户端
        client=FTPServer(connfd)
        client.setDaemon(True)
        client.start()

if __name__=="__main__":
    main()



