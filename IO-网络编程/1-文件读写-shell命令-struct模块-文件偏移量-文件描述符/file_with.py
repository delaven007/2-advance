"""
with 语句
"""

with open("text.txt") as f:  #生成f文件对象
    data = f.read()
    print(data)


#with  语句块结束   f   自动销毁