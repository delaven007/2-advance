"""
文件偏移
"""

# r,w 文件偏移量在开头
# a 文件偏移量在结尾
f= open("text.txt","wb+")
f.write(b"hell,oasdhdsff\n")
f.flush()
# f.close()

# print(f.tell())          #打印当前文件偏移量

f.seek(-7,1)               #以开头为基准向后移动0字节
f.seek(3,0)
# f= open("text.txt","r+")
data=f.read()
print(data)