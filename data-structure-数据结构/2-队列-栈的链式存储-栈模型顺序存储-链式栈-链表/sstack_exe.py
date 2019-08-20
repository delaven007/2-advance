# 一段文字，在文字中可能存在括号配对错误的情况，
# 要求写一段代码，检测文字中括号有没有错误
# 包括{} []  ()
from day2.ssetack import *

text = """达内时代科技集团有限公司
电话：010-62113433；400(-111-)8989
传真：010-{62110873}
邮编：100098
地址：[北京市海淀区北三环西路甲18号（大钟寺附近）]中坤广场E座10层10017室"""
parens = "{}[]()"
left_par = "{[("
right_par = "}])"
# 验证配对是否正确
correct_oppostite = {"}": "{", "]": "[", ")": "("}
st=SStack()
# 负责提供遍历到的括号

def parent(text):
    """
    遍历字符串，提供括号和位置
    """
    # i 记录索引位置
    i, text_len = 0, len(text)
    while True:
        # 循环遍历字符串遇到结尾结束，遇到括号提供VER
        while i < text_len and text[i] not in parens:
            i += 1
            if i >= text_len:
                return
            else:
                yield text[i], i
                i += 1

# 字符是否匹配验证的工作
def ver():
    for pr, i in parent(text):
        if pr in left_par:
            st.push((pr, i))
        elif st.is_None() or st.pop()[0] != correct_oppostite[pr]:
            print("不匹配，出错位置%d" % i)
            break
    else:
        if st.is_None():
            print("全部匹配")
        else:
            p = st.top()
            print(p[0], p[1])



