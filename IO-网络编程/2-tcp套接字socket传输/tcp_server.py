"""
tcp 套接字服务端流程
重点代码

"""
import socket
#创建流式套接字
sockfd =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址
sockfd.bind(("localhost",6666))
#设置sockfd为监听套接字
sockfd.listen(9)
#等待处理客户端连接请求
while  True:
    print("等待连接......")
    try:
        connfd,addr = sockfd.accept()
        print("连接在",addr)
    except KeyboardInterrupt:
        print("服务端退出")
        break
    #消息收发
    while True:
        data=connfd.recv(2048)
        # 设置循环结束条件：直接回车
        if not data:
            break
        print("Message",data.decode())
        n=connfd.send(b"** Clear **")
        print("发送%d bytes"%n)
    #关闭套接字
    connfd.close()               #断开连接
    break
sockfd.close()














