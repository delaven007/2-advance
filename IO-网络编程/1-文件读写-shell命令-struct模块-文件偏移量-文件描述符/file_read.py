"""
文件读取
"""

# 打开文件
# def open_file():
#     fd=open("dict.txt","r+")
#     while True:
#         #read读取文件，一次读取（2048）个字节
#         data=fd.read(2048)
#         #跳出循环
#         if not data:
#             break
#         print(data)

#总：文件是文本文件，打开方式可以是文本方式或者二进制方式，
# 如果文本方式打开，读写都是以字符串方式或读取或者写入内容：
#如果以二进制方式打开，读写都是以字符串读取或者写入内容
#如果文件是二进制文件，则打开方式必须以二进制打开，此时文件读写内容也是字节串

# data=fd.readline()
# print(data)
# data=fd.readline()
# print(data)

#读取所有内容，每行作为列表中一个元素
# data=fd.readlines(100)
# print(data)

#每次获取文件一行
# for line in fd:
#     print(line)
# fd.close()

#练习:从终端输入一个单词，打印出单词的解释，
# 如果没有该单词，print没有找到该单词

# while True:
#     word=input("word：")
#     fd = open("dict.txt")
#     for line in fd:
#         tmp=line.split(" ")[0]
#         #遍历的单词已经大于目标
#         if tmp > word:
#             print("没有找到该单词")
#             break
#         elif tmp == word:
#             print(line)
#             break
#     else:
#         print("没有找到该单词")
#     fd.close()

print("a"<"b")
