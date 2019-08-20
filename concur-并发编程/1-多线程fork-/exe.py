"""
创建父子进程，复制一个文件，
各自复制一半到新文件中
"""
import os
filename="./student.txt"
file_size=os.path.getsize(filename)
#父子进程使用fr会相互影响
# def reade_():
#     fr=open(filename,"rb")
#     return fr
def top():
    # fr=reade_()
    fr=open(filename,"rb")
    fw=open("top.txt","wb")
    n=file_size//2
    fw.write(fr.read(n))
    fr.close()
    fw.close()
def bot():
    # fr=reade_()
    fr=open(filename,"rb")
    fw=open("bot.txt","wb")
    fr.seek(file_size//2,0)
    fw.write(fr.read())
    fr.close()
    fw.close()

pid=os.fork()
if pid<0:
    print("Error")
elif pid==0:
    top()          #复制上半部分
else:
    bot()          #下半部分