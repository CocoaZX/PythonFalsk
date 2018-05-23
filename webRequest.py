# -- coding: utf-8 --
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Hossme</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001);

# from flask import Flask
#
# apps = Flask(__name__)
#
# @apps.route('/')
# # 捕捉url。此处为url无后缀
# def hello_world():
#     return '<h1> Love U Ma!</h1>'
#     # 返回header，只能有一个header
#
#
# if __name__ == '__main__':
#     apps.debug = True;
#     # 调试模式，开发使用
#
#     # app.run()
#     apps.run(host='0.0.0.0', port=1314);
#     #此处为全IP，端口为1314,
