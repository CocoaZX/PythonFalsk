from flask import Flask
import pymysql


app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

#打开数据库
db = pymysql.connect(host="127.0.0.1",user="root",password="12345678",db="mysql",port=3306)

#获取操作游标
cur = db.cursor()

if __name__ == '__main__':
    app.run()