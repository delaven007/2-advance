"""
1.文件函数使用熟练（open,read,write）
2.从终端输入一个文件名称（），
如果该文件存在则将该文件复制到当前目录下，命名为1904
要求文件可以是任意类型，如果文件不存在，打印文件不存在
"""

# filename=input("file_name：")
#
# try:
#     f=open(filename,"rb+")
#
# except FileNotFoundError as e:
#     print(e)
#
# else:
#     fw=open("file","wb")
#     while  True:
#         data=f.read(2048)
#         if not data:
#             break
#         fw.write(data)
#     f.close()
#     fw.close()


"""
    *文件打开方式
3.向一个文件写入日志，写入格式：
1.2019-1-1 12:12:12
1.2019-1-1 12:12:13
10s
3.2019-1-1 12:12:23
要求每隔一秒写入一次，每条时间占一行
程序死循环，如果程序退出，
重新启动时，要求内容能跟上次内容衔接
"""
import time
f=open("text,txt","a+")
n=0
f.seek(0,0)          #将偏移量移动到开始然后计数
for line in f:
    n +=1
while  n<100:
    n+=1
    time.sleep(1)
    s=("%d  %s\n"%(n,time.ctime()))
    f.write(s)
    f.flush()    #随时看到文件变化
else:
    f.close()