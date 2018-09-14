from flask import Flask
import pymysql


app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

#打开数据库
db = pymysql.connect(host="47.106.99.78",user="root",password="20Miqianlan",db="mysql",port=3306)

#获取操作游标
cur = db.cursor()

if __name__ == '__main__':
    app.run()