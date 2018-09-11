from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
# import MySQLdb



# -*- coding:utf-8 -*-# config.pyDIALECT = 'mysql'DRIVER = 'pymysql'USERNAME = 'root'PASSWORD = 'root'# HOST = '127.0.0.1'    # 自己电脑的ip 或者localhostHOST = 'localhost'      # 自己电脑的ipPORT = '3306'           # MySQL默认的端口号DATABASE = 'db_demo1'# SQLALCHEMY_DATABASE_URI = '[数据库名]+[数据库中间件(驱动)]://[用户名]:[password]@[主机IP地址]:[端口号]/[数据库名字]?charset=utf8'# SQLALCHEMY_TRACK_MODIFICATIONS = True# 数据库连接必须用这个名字  SQLALCHEMY_DATABASE_URISQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
# -*- coding:utf-8 -*-# db_test.pyfrom flask import Flaskfrom flask_sqlalchemy import SQLAlchemyimport config

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

db.create_all()@app.route('/')
    def index():
    return 'index'



# import pymysql
# #创建连接
# conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db="test");
# #创建游标
# cursor = conn.cursor()
# #执行sql，并返回受影响的行数
# effect_row = cursor.execute("select * from student")
# print(effect_row)

# sql expresstion 可以通过一些表达式书写sql。但是不是ORM。
# engine = create_engine("mysql://root:@localhost:3306/webpy?charset=utf8",encoding="utf-8", echo=True)#
#数据库类型://用户名:密码（没有密码则为空，不填）@数据库主机地址/数据库名?编码
#echo = True 是为了方便 控制台 logging 输出一些sql信息，默认是False


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/test?charset=utf8mb4'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#
# db = SQLAlchemy(app)
#
#
# with app.app_context():
#     db.drop_all()
#     db.create_all()
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(320), unique=True)
#     password = db.Column(db.String(32), nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username

if __name__ == '__main__':
    app.run()