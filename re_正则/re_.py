import re
#
# s="赵丽颖：1987,古力娜扎：1992"
#
# re_.findall("\d+", s)

s="Alex:1994,Sunny:1993"
pattern =r"\w+:\d+"

#re模块调用findall
# l=re.findall(pattern, s)
# print(l)

#使用compile对象调用
regex = re.compile(pattern)
l=regex.findall(s)
print(l)


#按照匹配到的内容切割字符串
l=re.split(r"[:,]",s)
print(l)

#替换匹配到的内容
s=re.subn(r"\s+","#","He is a boy")
print(s)

#提取出一段文字中所有的日期（2019-05-23）
#将日期打印出来，打印格式（2019/05/23）
l=("赵云去世后，于蜀汉景耀四年（1995-05-23）被追谥为“顺平候”，2097-05-12其“常胜将军”的形象在后世被广为流传。")
n=re.findall(r"\d{4}-\d{1,2}-\d{1,2}",l)
print(n)
for i in n:
    print(re.sub(r"-","/",i))


