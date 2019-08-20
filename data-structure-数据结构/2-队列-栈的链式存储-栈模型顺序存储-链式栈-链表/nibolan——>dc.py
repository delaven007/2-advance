from day2.lstack import *
# from day1.linklist import *
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


























