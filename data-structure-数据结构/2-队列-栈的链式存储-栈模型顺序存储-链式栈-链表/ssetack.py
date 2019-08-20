"""
sstack   栈模型顺序存储
思路分析：
1.列表即顺序存储，但功能太多，不符合栈模型
2.利用列表，封装类，提供栈的接口方法
"""
#自定义异常
class StackError(Exception):
    pass


#顺序栈类封装
class SStack:
    def __init__(self):
        #属性为控列表，这个列表就是栈的存储空间
        #列表最后一个为栈顶元素
        self._elems=[]

    def is_None(self):
        return self._elems==[]

    #入栈
    def push(self,data):
        self._elems.append(data)
    #出栈
    def pop(self):
        #self._elems为空，执行异常
        return self._elems.pop()        #弹出列表最后一个

    #查看栈顶元素
    def top(self):
        if self._elems ==None:
            raise StackError("stack is empty")
        return self._elems[-1]

if __name__ =="__main__":
    st=SStack()               #初始化
    st.push(50)
    st.push(100)
    st.push(1345310)
    while not st.is_None():
        print(st.pop())
