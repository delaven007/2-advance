# from socket  import *
import re
#
# ADDR=("localhost",6060)
#
# fd=socket()
# fd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# fd.bind(ADDR)
# fd.listen(1)
#
# # class udp_server():

# def handle(port):
#     fd = open("exc.txt","r")
#     fl=fd.read().split("\n\n")
#     fl.remove(fl[0])
#     fl.split()
#     for i in fl:
#        value=re.split(r"\waddress is")
#














        # fd = open("exc.txt", "rb")
        # for line in fd:
        #     line_s = line.split(" ")[0]
        #     idex = re.finditer(r"\w+", fd)
        #     value = re.finditer(r"\d+", fd)
        #     if line_s == "value":
        #         fd.get_address(addr)
        #     else:
        #         continue







#
# def main():
#     while   True:
#         try:
#             print("等待连接...")
#             connfd, addr = fd.accept()
#
#         except KeyboardInterrupt:
#             print("服务器退出")
#         except Exception as e:
#             print(e)
#         else:
#             while True:
#                 data,addr=fd.recvfrom(4096)
#                 if not data:
#                     break
#                 elif data=="OK":
#                     fd.sendto("recive".encode(),addr)
#                     fd.handle(fd)
# if __name__=="__main__":
#     main()




