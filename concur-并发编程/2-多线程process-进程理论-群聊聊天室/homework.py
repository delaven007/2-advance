"""
1.将父子进程copy文件，变成process完成
2.将fork和process比较
3.函数和类的使用
4.聊天室总结
"""
import os
from multiprocessing import Process
file_name="./dict.txt"
file_size=os.path.getsize(file_name)

def top():
    fr=open(file_name,"r")
    fw=open("top.txt","w")
    n=file_size//2
    fw.write(fr.read(n))
    fr.close()
    fw.close()
def bot():
    fr=open(file_name,"r")
    fw=open("bot.txt","w")
    n=file_size//2
    fw.write(fr.read(n))
    fr.close()
    fw.close()
p=Process(target=top)
p.start()
p.join()
d=Process(target=bot)
d.start()
d.join()