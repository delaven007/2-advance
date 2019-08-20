"""
squue.py     队列的顺序存储
重点代码

思路解析：
1.基于列表完成存储结构
2.通过封装规定对头和队尾操作

"""
class QueueError(Exception):
    pass
#队列操作类
class SQueue:
    def __init__(self):
        self._elems=[]

    #判断队列空
    def is_empty(self):
        return self._elems==[]

    #入队
    def enqueue(self,elem):
        self._elems.append(elem)

    #出队
    def dequeue(self):
        if self._elems == []:
            raise QueueError("队列为空")
        return self._elems.pop(0)
if __name__=="__main__":
    sq=SQueue()
    sq.enqueue(5)
    sq.enqueue(6)
    sq.enqueue(9)
    sq.is_empty()
    while not sq.is_empty():
        print(sq.dequeue())
