"""
pymysql 操作数据库基本流程
"""

import pymysql

#建立数据库链接
db=pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",database="stu",charset="utf8")
#创建游标(由于进行数据操作的对象,承载操作结果)
cur=db.cursor()

#执行SQL语句
sql="insert into student (name,age,gender,score) values('王大锤',25,'w',67.5);"
cur.execute(sql)
db.commit() #将写操作提交到数据库

#关闭数据库
cur.close()
db.close()
