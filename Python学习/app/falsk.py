# -*-coding:utf-8-*-

#常用HTTP响应

from SQL.ext import db
from SQL.users import User
import os
from flask import Flask , request ,redirect ,abort, send_from_directory,make_response


app = Flask(__name__,static_url_path='/Users/zhangxin/Desktop/PythonFalskGit/Python学习/static')#传name是为了定位程序的根目录。找到相对应资源的相对位置。和xcode中的文件项目找path是一样的。
app.config.from_object('SQL.consts')
db.init_app(app)

#abort抛出异常
@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name

def load_user(id):
    return ''


#重定向,可以不用flask的方法。直接使用返回302
@app.route('/redeirect')
def index():
    return redirect('http://www.example.com')


#可以返回http状态码，header等。此处返回设置cookie
@app.route('/cookie')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

#app程序上下文，会在实例调用之后触发
with app.app_context():
    db.drop_all()
    db.create_all()

@app.route('/')#处理URL和函数之间的关系称为路由.
# 捕捉url。此处为url无后缀
def hello_world():
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir,'static'),'example.html')
    # return '<h1> k</h1>'
    # 返回header，只能有一个header

#request 虽然写的是全局变量，但实际上是捕获上下文的特定变量。否则多线程全是一个变量肯定不可能
#类似的上下文关键字还有:
# cueetn_app 程序上下文.获取当前程序实例
# g 处理请求时用的临时存储对象
# session  用户会话，储存请求之间的值哈希字典类型
@app.route('/users/<name>',methods=['POST'])#尖括号内为动态部分，匹配到静态部分的URL都会印射到这个路由上
def users():
    user_agent = request.headers.get('User-Agent')
    print(user_agent)
    username = request.from_values('name')
    user = User.__init__(username)
    print('User ID:{}'.format(user.id))#还没有创建id都是none
    db.session.add(user)
    db.session.commit()


@app.route('/people')
def people():
    name = request.args.get('name')


#确认是运行__main__函数才run，而不是导入的时候,或者父级脚本执行,启动后会进入轮询直到停止
if __name__ == '__main__':
    app.debug = True;
    # 调试模式，开发使用
    # app.run()
    app.run(host='0.0.0.0', port=12333);
    #此处为全IP，端口为1314,®外网可以访问到