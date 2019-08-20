from socket import *
import sys

HOST="127.0.0.1"
PAST=9898
ADDR=(HOST,PAST)
ftp="/home/tarena/1904/"
class FTPClient():
    def __init__(self,s):
        self.s=s

    def do_list(self):
        self.s.send("L".encode())
        data=self.s.recv(4096).decode()
        if data=="OK":
            data=self.s.recv(8192)
            print(data.decode())
        else:
            print(data)

    def do_get(self,filename):
        self.s.send(("G"+filename).encode())
        data=self.s.recv(4096).decode()
        if data=="OK":
            f=open(filename,"wb")
            while  True:
                self.s.recv(8192)
                if data=="##".encode():
                    break
                f.write(data)
            f.close()
        else:
            print(data)


    def do_quit(self):
        self.s.send("Q".encode())
        self.s.close()
        sys.exit()

def main():
    s=socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print(e)
        return
    print("连接成功")

    ftp=FTPClient(s)

    while True:
        print(""""\n--------------命令选项---------------------
                   ****             list                   ****
                   ****           get filename          ****
                   ****           put filename             ****
                   ****             quit                   ****
                    ------------------------------------------\n""")
        cmd=input("请输入(list,get,put,quit):")
        if cmd.strip()=="list":
            ftp.do_list()
        elif cmd[:3]=="get":
            filename=cmd.strip().split(" ")[-1]
            ftp.do_get(filename)

        elif cmd.strip()=="quit":
            ftp.do_quit()


if __name__=="__main__":
    main()