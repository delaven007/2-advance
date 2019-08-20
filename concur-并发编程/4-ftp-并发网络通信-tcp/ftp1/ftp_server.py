from threading import Thread
from socket import *
import os
from time import sleep

HOST = "localhost"
PAST = 9898
ADDR = (HOST, PAST)

ftp = "/home/tarena/ftp/"


# FTP服务端类
class FTPSERVER(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()

    # 查看
    def do_list(self):
        files = os.listdir(ftp)
        if not files:
            self.connfd.send("文件库为空".encode())
        else:
            self.connfd.send("OK".encode())
            sleep(0.01)
        file_ = ""
        for file in files:
            if file[0] != "." and os.path.isfile(ftp + file):
                file_ += file + "\n"
        self.connfd.send(file_.encode())

    # 下载
    def do_get(self, filename):
        try:
            fd = open(ftp + filename, "rb")
        except Exception:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send("OK".encode())
            sleep(0.1)
        while True:
            data = fd.read(4096)
            if not data:
                sleep(0.01)
                self.connfd.send("##".encode())
                break
            self.connfd.send(data)

    # 上传
    def do_put(self):
        pass

    # 循环接收
    def run(self):
        while True:
            data = self.connfd.recv(4096).decode()
            if not data and data == "Q":
                return
            elif data == "L":
                self.do_list()
            elif data[0] == "G":
                filename = data.split(" ")[-1]
                self.do_get(filename)


def main():
    fd = socket()
    fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    fd.bind(ADDR)
    fd.listen(1)
    print("监听端口：%d", PAST)

    while True:
        try:
            connfd, addr = fd.accept()
        except KeyboardInterrupt:
            print("服务器退出")
            return
        except Exception as e:
            print(e)
            continue

        client = FTPSERVER(connfd)
        client.setDaemon(True)
        client.start()


if __name__ == "__main__":
    main()
