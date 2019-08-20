import pymysql
import re

fd = open("dict.txt","r")
#建立数据库链接
db=pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",database="dict",charset="utf8")
#创建游标(由于进行数据操作的对象,承载操作结果)
cur=db.cursor()


sql = "insert into words (word,mean) values(%s,%s)"

for line in fd:
    #获取word和mean
    tup=re.findall(r"(\S+)\s+(.*)",line)[0]
    try:

        cur.execute(sql,tup)
        db.commit()            #可以执行多个sql语句一同提交
    except:
        db.rollback()          #退回到commit之前的操作
#关闭数据库
cur.close()
db.close()
