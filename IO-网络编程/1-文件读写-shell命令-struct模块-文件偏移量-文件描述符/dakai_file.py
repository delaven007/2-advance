"""
file_open.py  打开文件
"""
#打开文件
try:
    fd=open("text1.txt","a+")
except FileNotFoundError as e:
    print(e)

#开始你的读写
#关闭文件
fd.close()
