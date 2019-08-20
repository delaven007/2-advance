"""
finditer 使用
"""
import  re
s="2019年，建国70年"
patter=r"\d+"
#返回迭代器
idex=re.finditer(patter,s)

# print(dir(idex.__next__()))
for i in idex:
    # print(i)
    print(i.group())    #获取match对象

#完全匹配
m=re.fullmatch(r"\w+","Jame1")
print(m)

#匹配开始位置
n=re.match(r"[A-Z]\w*","Hello Kitty")
print(n)
#匹配第一个
n=re.search(r"[A-Z]\w*","Hello Kitty")
print(n)
