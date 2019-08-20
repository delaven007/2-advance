"""
写入文件
"""
#原有内容被清除
# f=open("text.py","w")
# f.write("hello python\n")
# f.write("哎呀，干哈呀")
# f.close()
#


# f=open("text.py","wb")
# #wb打开要转换成字节串写入
# f.write("hello python\n".encode())
# f.write("哎呀，干哈呀\n".encode())
# f.write("哎呀，干哈呀".encode())
# f.close()

#w原有内容被清除，a则追加
f=open("text.py","a")
#wb打开要转换成字节串写入
f.writelines(["abc\n","def\n"])
f.writelines(["9213\n","def\n"])

f.close()