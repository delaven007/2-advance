
text='''首页免费课直播课会员课培优课线上班（VIP）线下班最新活动我的课程 
您想学的课程前{端/后端开发大[数据/云计算移动开发/游戏物联网/测试营销/产品]/运营 
数字艺术其他职业课(程加入会员超值会员权益手机绑定得资料下载权限单报名获}赠平
安就业险帮助页面带你玩转TMOOC 我的课程 查看更多>>方向：AID
班级：AIDTN190429距离有效期截止还剩3月1)6天Python基础入门
免费5677人报名 直播课 查看更多>>GlusterFS分布式文件系统
免费1,166人报名快速学会PS的2种操作8大技能（添加客服免费领取）
￥59.0[04,317人购{买商业插画-板绘潮流Q版角色之复仇}者联盟体]验课
免费1,(5{0[6人报]}名SEO排名利剑，专题单页优化
￥199.001,542人购买Py)thon基础入门
免费5,665人报名会员课 查看更多>>
一周上手小程序1.00（会员免费）4,761人报名
商业插画零(基础手绘教程599.00（会员免费）2,)962人报名'''


parens = "{}[]()"  #　需要验证的字符
left_parens = "{[("
#　验证配对是否正确
opposite = {'}':'{',']':'[',')':'('}

st = SStack() #　初始化一个栈

# 负责提供遍历到的括号
def parent(text):
  """
  遍历字符串,提供括号字符和其位置
  """
  #　ｉ记录索引位置
  i,text_len = 0,len(text)
  while True:
    # 循环遍历字符串
    # 到结尾结束，遇到括号提供给ｖｅｒ
    while i < text_len and text[i] not in parens:
      i += 1

    if i >= text_len:
      return
    else:
      yield  text[i],i
      i += 1


#　字符是否匹配的验证工作
def ver():
  for pr, i in parent(text):
    if pr in left_parens:
      st.push((pr,i))  #　左括号入栈
    elif st.is_empty() or st.pop()[0] != opposite[pr]:
      print("Unmatching is found at %d for %s"%(i,pr))
      break
  #　ｆｏｒ循环正常结束
  else:
    if st.is_empty():
      print("All parentheses are matched")
    else:
      #　剩下左括号了
      p = st.pop()
      print("Unmatching is found at %d for %s" % (p[1], p[0]))

# 主程序只负责做括号的验证
ver()















