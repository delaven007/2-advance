import struct
st=struct.Struct("i4sf")
data=st.pack(1,b"lily",1.68)
# data=st.pack(1,b"zhangsan",1.68)
st.unpack(data)
print(st)
print(struct.pack("i5sf",2,b"zhang",1.8))

#-------------------------------------------------------
"""
从客户端输入学生信息，包含 编号（整形）姓名（str） 
 年龄（整形）分数（浮点，精确小数点后一位），将其发送服务端

服务端接受到的内容写入到一个文件里，每个学生信息占一行
"""
