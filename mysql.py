"""
pymysql
"""
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

# 获取游标
cur = db.cursor()

# 执行sql
sql = "insert into class_1 values(3,'Emma', 17,'w',76.5,'2019-8-8');"

# 执行语句
cur.execute(sql)

# 将写操作提交,多次写操作一次提交
db.commit()

cur.close()
db.close()
