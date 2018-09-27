
# from flask import Flask
from SQL.consts import HOSTNAME,USERNAME,PASSWORD,DATABASE,PORT
import pymysql


#打开数据库
db = pymysql.connect(host=HOSTNAME,user=USERNAME,password=PASSWORD,db=DATABASE,port=PORT)


#游标实际上是一种能从包括多条数据记录的结果集中每次提取一条记录的机制。相当于C语言的语句句柄
cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print('Database version : %s' %data)

db.close()

# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return 'index'
#
#
# if __name__ == '__main__':
#     app.run()