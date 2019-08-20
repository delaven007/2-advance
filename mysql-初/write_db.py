"""
mysql 数据库写操作练习
* 增删改为写操作
"""
"""
pymysql 操作数据库基本流程
"""
import pymysql
import re

fd = open("dict.txt","r")
#建立数据库链接
db=pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",database="stu",charset="utf8")
#创建游标(由于进行数据操作的对象,承载操作结果)
cur=db.cursor()

#执行SQL语句
try:
    #插入数据
    # name=input("name:")
    # age=int(input('age:'))
    # gender=input('gender:')
    # score=float(input('score:'))
    #
    # sql="insert into student (name,age,gender,score) values('%s',%d,'%s',%f)"%(name,age,gender,score)
    # sql="insert into student (name,age,gender,score) values(%s,%s,%s,%s)"
    # sql="insert into interest values (3,'Joy','sing','B',5488.0,'画的鸟蛋还行')"

    # cur.execute(sql)
    # cur.execute(sql,[name,age,gender,score])
    # sql=

    while True:

        for line in fd:
            words=line.split(" ")[0]
            mean=line.split(" ")[1]
            if not words:
                break

    sql="insert into dict_1 (words,mean) values(%s,%s)"
    cur.execute(sql,[words,mean])

    #修改操作
    # sql="update student set age=22 where name = 'Monika'"

    #删除操作
    # sql="delete from student where score < 81"


    cur.execute(sql)

    db.commit()            #可以执行多个sql语句一同提交
except Exception as e:
    db.rollback()          #退回到commit之前的操作
    print(e)
#关闭数据库
cur.close()
db.close()
