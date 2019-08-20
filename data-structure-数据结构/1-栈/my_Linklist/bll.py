from day1.my_Linklist.model import Node

class Linklist:
    """
    建立链表模型
    操作
    """
    def __init__(self):
        """
        初始化链表，生成头结点
        """
        self.head=Node(None)
    def init__list(self,list_):
        """
        添加一组链表结点
        :param list_:
        :return:
        """
        p=self.head             #创建一个移动变量
        for item in list_:
            p.next=Node(item)
            p=p.next           #向后移动一个结点
    #遍历
    def show(self):
        p=self.head.next         #第一个结点
        # while p!=None:
        while p is not None:
            print(p.data,end=" ")
            p=p.next
        print()                   #换行

    #获取链表长度
    def get_lenth(self):
        n=0
        p=self.head.next
        while p is not None:
            n+=1
            p=p.next
        return n

    #判断链表长度
    def is_None(self):
        if self.get_lenth() ==0:
            return True
        else:
            return False

    #清空链表
    def clear(self):
        self.head.next=None

    #尾部增加新节点
    def append(self,value):
        p=self.head
        while p.next is not None:
            p=p.next
        p.next=Node(value)
    def insert(self,Index,data):
        """
        选择位置插入节点
        :param node2:
        :return:
        """
        if Index < 0 or Index > self.get_lenth():
            raise IndexError("index out of range")
        p=self.head
        for item in range(Index):
            p=p.next

        node=Node(data)
        node.next=p.next
        p.next=node
    def delete(self,data):
        """
        删除节点
        :return:
        """
        p=self.head
        while p.next and p.next.data != data:
            p=p.next
        #判断while循环结束原因
        if p.next is None:      #判断删除的节点是否存在
            raise ValueError("value is out of range")
        p.next=p.next.next

    #获取节点值
    def get_item(self,index):
        if index < 0 or index >= self.get_lenth():
            raise IndexError("index out of range")
        p=self.head.next
        for item in range(index):
            p=p.next
            return p.data