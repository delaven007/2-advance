"""
ftp 客户端
"""
from socket import *
import sys
from time import sleep

HOST="localhost"
PORT=9898
ADDR=(HOST,PORT)  #服务器地址
ftp="/home/tarena/1904/"

#客户端功能处理类
class FTPClient:
    def __init__(self,sockfd):
        self.sockfd=sockfd
    #查看列表
    def do_list(self):
        self.sockfd.send("L".encode())    #发送请求
        #等待回复
        data=self.sockfd.recv(4096).decode()
        if data =="OK":
            #一次接受文件列表字符串
            data=self.sockfd.recv(8192)
            print(data.decode())
        else:
            print(data)
    #下载
    def do_get(self,filename):
        #发送请求
        self.sockfd.send(("G "+filename).encode())
        #等待回复
        data=self.sockfd.recv(4096).decode()
        if data=="OK":
            fd=open(filename,"wb")
            #接收文件
            while True:
                data=self.sockfd.recv(4096)
                if data=="##".encode():
                    break
                fd.write(data)
            fd.close()
        else:
            print(data)

    #上传
    def do_put(self,filename):
        # 发送请求
        self.sockfd.send(("P " + filename).encode())
        # 等待回复
        try:
            fd=open(ftp+filename, "rb")   #上传的文件位置ftp
        except Exception:
            print("上传文件不存在")
            return
        else:
            while True:
                data=fd.read(4096)
                if not data:
                    sleep(0.1)
                    self.sockfd.send(b"##")
                    break
                self.sockfd.send(data)
            fd.close()

    #退出
    def do_quit(self):
        self.sockfd.send("Q".encode())
        self.sockfd.close()
        sys.exit("谢谢使用")

#创建客户端网络
def main():
    sockfd=socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return
        #循环发送请求
    print("连接成功")

    ftp = FTPClient(sockfd)       #实例化对象

    #循环发送请求
    while True:
        print(""""\n--------------命令选项---------------------
                   ****             list                  ****
                   ****           get file                 ****
                   ****           put file                 ****
                   ****             quit                   ****
                    ------------------------------------------\n""")

        cmd=input("输入命令(list,get,put,quit)：")
        if cmd.strip()=="list":
            ftp.do_list()
        elif cmd[:3] =="get":
            #get file name
            filename=cmd.strip().split(" ")[-1]
            ftp.do_get(filename)
        elif cmd[:3] =="put":
            #put file name
            filename=cmd.strip().split(" ")[-1]
            ftp.do_put(filename)
        elif cmd.strip()=="quit":
            ftp.do_quit()

        else:
            print("请输入正确命令")

if __name__=="__main__":
    main()