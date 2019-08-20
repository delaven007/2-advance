"""
bittree ：二叉树的实现

思路分析：
1.使用链式存储
    节点类设计上有两个属性变量引用左孩子和右孩子
2.操作类完成二叉树的遍历
"""
from day2.dui_lie import SQueue
class BitreeError(Exception):
    pass

#二叉树节点
class TreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

#二叉树的操作
class Bitree:
    def __init__(self,root=None):
        self.root=root   #获取树根


    #先序遍历
    def preOrder(self,node):
        if node is None:
            return
        print(node.data,end=" ")
        self.preOrder(node.left)
        self.preOrder(node.right)

    # 中序遍历
    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.data, end=" ")
        self.inOrder(node.right)

    # 后序遍历
    def outOrder(self, node):
        if node is None:
            return
        self.outOrder(node.left)
        self.outOrder(node.right)
        print(node.data, end=" ")

    #层次遍历
    def levelOrder(self,node):
        sq=SQueue()
        sq.enqueue(node)           #遍历
        while not sq.is_empty():
            node=sq.dequeue()
            print(node.data,end=" ")    #出队
            if node.left:
                sq.enqueue(node.left)
            if node.right:
                sq.enqueue(node.right)

if __name__=="__main__":
    #后序遍历
    b=TreeNode("B")
    f=TreeNode("F")
    g=TreeNode("G")
    d=TreeNode("D",f,g)
    i=TreeNode("I")
    h=TreeNode("H")
    e=TreeNode("E",h,i)
    c=TreeNode("C",d,e)
    a=TreeNode("A",b,c)         #树根
    #初始化数对象，得到树根
    bt=Bitree(a)
    # #先序
    bt.preOrder(bt.root)
    print()
    # #中序
    bt.inOrder(bt.root)
    print()
    #
    # #后序
    bt.outOrder(bt.root)

    # bt.levelOrder(bt.root)
