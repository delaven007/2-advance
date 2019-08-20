# file_name=input("filename：")
# try:
#     f=open(file_name,"rb+")
# except FileNotFoundError as e:
#     print(e)
# else:
#     fw=open(file_name,"wb+")
#     while True:
#         data=fw.read()
#         if not data:
#             break
#         fw.write(data)
#     fw.close()
#     f.close()
#***************************************
import time
f=open("text,txt","a+")
n=0
f.seek(0,0)
for line in f:
    n+=1
while  n<100:
    n+=1
    time.sleep(1)
    s=("%d,%s\n"%(n,time.ctime()))
    f.write(s)
    f.flush()
f.close()