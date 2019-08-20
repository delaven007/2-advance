"""
栈的链式存储

重点

思路与分析：
1.基本的实现模型源于 链表
2.栈顶位置
"""
#自定义异常
class StackError(Exception):
    pass

# 节点类
class Node:
    """
    节点类
    """

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# 栈操作类
class Lstack:
    def __init__(self):
        # 定义栈顶
        self.__top = None
        # self.next = None
    #判断是否为空
    def is_empty(self):
        return self.__top is None
    #输出栈
    def push(self, elem):
        self.__top = Node(elem, self.__top)
    #弹出栈
    def pop(self):
        if self.__top is None:
            raise StackError("栈为空")
        val = self.__top.data
        self.__top = self.__top.next
        return val

    #   查看栈顶值
    def top(self):
        if self.__top is None:
            raise StackError("栈为空")
        return self.__top.data

# if __name__ == "__main__":
#     ls = Lstack()
#     ls.push(10)
#     ls.push(50)
#     ls.push(90)
#     print(ls.top())
#     ls.pop()
#     print(ls.top())
ls=Lstack()
while True:
    exp=input()
    tmp=exp.split(" ")
    for item in tmp:
        if item  not in ("+","-","p"):
            ls.push((float(item)))      #数字入栈
        elif item =="+":
            x=ls.pop()
            y=ls.pop()
            ls.push(y+x)
        elif item == "-":
            x=ls.pop()
            y=ls.pop()
            ls.push(y-x)
        elif item == "p":
            if ls.pop():
                print(ls.top())
            print(ls.top())
