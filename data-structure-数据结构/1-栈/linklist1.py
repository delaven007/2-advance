class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Linklist:
    def __init__(self):
        self.head=None

    def append(self,data):
        """
        添加一个
        :param data:
        :return:
        """
        p=self.head
        while p.next==None:
            p.next=Node(data)

    # 删除
    def delete(self,data):
        p=self.head
        while p.next and p.next.data!=data:
            p=p.next
        if p.next==None:
            raise IndexError("删除的数据不存在")
        p.next=p.next.next
    #显示
    def show(self):
        p=self.head.next
        while p is not None:
            print(p.data,end=" ")
            p=p.next
        print()

    def get_linklength(self):
        n=0
        p=self.head.next
        while p is not None:
            n+=1
            p=p.next
        return n

    #判断链表长度
    def is_None(self):
        if self.get_linklength():
            return True
        else:
            return False

