"""
lqueue.py 链式队列
重点代码

思路分析：
1.基于列表完成链式栈
2.链表开端作为对头，尾端作为队尾
"""
#队列异常
class QueueError(Exception):
    pass
class Node:
    """
    节点类
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#链式队列
class LQueue:
    def __init__(self):
        self.front=self.rear=Node(None)
    def is_empty(self):
        return self.front==self.rear
    #入队
    def enqueue(self,elem):
        self.rear.next=Node(elem)
        self.rear=self.rear.next

    #出对
    def dequeue(self):
        if self.front==self.rear:
            raise QueueError("队列为空")
        self.front=self.front.next
        return self.front.data
if __name__=="__main__":
    lq=LQueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    print(lq.dequeue())