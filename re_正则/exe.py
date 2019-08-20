"""
1.熟练元字符的使用
2.re模块
3.通过分析文档使用正则完成接口编写，从终端输入端口名，返回address地址
"""
import re

def find(port):
    fd = open("exc.txt", "r")
    fl = fd.read().split("\n\n")
    fl.remove(fl[0])
    fl.split()
    for i in fl:
        value = re.split(r"\waddress is")