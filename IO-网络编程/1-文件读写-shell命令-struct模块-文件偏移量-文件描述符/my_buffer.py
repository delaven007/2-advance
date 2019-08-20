"""
buffer    缓冲区f.flush
"""
f=open("text.txt","w")
while True:
    s=input(">>")
    f.write(s)
    f.flush()  #将缓冲内容写入磁盘

f.close()



