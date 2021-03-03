"""
单词本插入数据库
"""
import pymysql
import re

f = open('dict.text') # 打开文件
# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

# 获取游标
cur = db.cursor()

# data = f.readline()
# tmp = data.split(' ')
# word = tmp[0]
# mean = ' '.join(tmp[1:]).strip()
sql = "insert into words (word,mean) values(%s,%s)"

for line in f:
    tup = re.findall(r'(\S+)\s+(.*)',line)[0]
    try:
        cur.execute(sql, tup)
        db.commit()
    except:
        db.rollback()

f.close()
cur.close()
db.close()
