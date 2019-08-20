"""
使用示例
"""
import re
pattern = r"(ab)cd(?P<pig>ef)"
regxt=re.compile(pattern)
obj=regxt.search("abcdefghi")     #match对象
#属性变量
print(obj.pos)          #开头位置
print(obj.endpos)         #结尾位置
print(obj.re)           #正则
print(obj.string)       #目标字符串
print(obj.lastgroup)      #最后一组组名
print(obj.lastindex)        #最后一组序列号
#属性方法
#匹配内容在目标字符串的位置
print(obj.span())
print(obj.start())
print(obj.end())
#捕获组字典
print(obj.groupdict())
#子组内容
print(obj.groups())
#获取匹配内容
print(obj.group())




