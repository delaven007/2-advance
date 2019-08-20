import socket
import struct
socketfd=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

socketfd_addr=("localhost",6666)
# socketfd.connect((socketfd_addr))
#格式与服务端一致
st=struct.Struct("i32sif")

while True:
    print("===========================================")
    id=int(input("ID:"))
    name=(input("name:").encode())
    age=int(input("Age:"))
    score=float(input("Score:"))
    #打包
    data=st.pack(id,name,age,score)
    socketfd.sendto(data,socketfd_addr)

socketfd.close()