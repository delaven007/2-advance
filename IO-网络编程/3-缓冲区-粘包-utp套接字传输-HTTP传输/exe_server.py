from socket import *

DICT_TEXT="./dict.txt"
def find_word(word):
    data = open("DICT_TEXT", "r")
    # if data is None:
    #      break
    for line in data:
        tmp = line.split(" ")[0]
        # 遍历的单词已经大于目标
        if tmp > word:
            return "没有找到该单词"

        elif tmp == word:
            return line
    else:
        return ("没有找到该单词")
#创建套接字
socketfd=socket(AF_INET,SOCK_DGRAM)
#绑定地址
server_addr=(("localhost",6666))
socketfd.bind(server_addr)

#收发消息
while True:
    data1,addr=socketfd.recvfrom(8192)
    mean=find_word(data1.decode())
    socketfd.sendto(mean.encode(),addr)
#关闭套接字
    socketfd.close()