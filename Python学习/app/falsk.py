# -*-coding:utf-8-*-

from SQL.ext import db
from SQL.users import User
import os
from flask import Flask , request , jsonify , send_from_directory


app = Flask(__name__,static_url_path='/Users/zhangxin/Desktop/PythonFalskGit/Python学习/static')
app.config.from_object('SQL.consts')
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

@app.route('/')
# 捕捉url。此处为url无后缀
def hello_world():
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir,'static'),'example.html')
    # return '<h1> k</h1>'
    # 返回header，只能有一个header


@app.route('/users',methods=['POST'])
def users():
    username = request.from_values('name')
    user = User.__init__(username)
    print('User ID:{}'.format(user.id))#还没有创建id都是none
    db.session.add(user)
    db.session.commit()


#确认是运行__main__函数才run，而不是导入的时候
if __name__ == '__main__':
    app.debug = True;
    # 调试模式，开发使用
    # app.run()
    app.run(host='0.0.0.0', port=12333);
    #此处为全IP，端口为1314,®外网可以访问到