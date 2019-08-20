"""
pymysql 存储二进制文件
"""
import pymysql

#建立数据库链接
db=pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",database="stu",charset="utf8")
#创建游标(由于进行数据操作的对象,承载操作结果)
cur=db.cursor()

# #存储文件
# with open('img.jpg','rb') as fd:
#     data=fd.read()
# try:
#     sql="insert into Image values(1,'i.jpg',%s)"
#     cur.execute(sql,[data])
#     db.commit()
# except:
#     db.rollback()

# 获取图片
sql="select * from Image where filename='i.jpg'"
cur.execute(sql)


img=cur.fetchone()
with open(img[1],'wb') as f:
    f.write(img[2])

#关闭数据库
cur.close()
db.close()