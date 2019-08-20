"""
1.编写函数，传入一个整数，反回该整数的阶乘
2.将线性代码整理
"""
# import os
# print (os.sys.path)
import sys

sys.path.append('/home/aaa/1python/1904/month01/python_date_structure/day2')


# def get_factorial(n):
#     if n<0:
#         exit()
#     sum = 1
#     for i in range(2,n+1):
#         sum =sum*i
#     print(sum)
#     return
#
# get_factorial(3)


# def get_factorial(n):
#     assert n >= 0
#     if n < 2:
#         return 1
#     else:
#         print(n * get_factorial(n - 1))
#
# get_factorial(3)

# simple

# x=1
# y=int(input("请输入要计算的数："))
# for i in range(1,y+1):
#     x=x*i
# print(x)

# 递归

# def func(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return (n*func(n-1))
# a=func(0)
# print(a)

