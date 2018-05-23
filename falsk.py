
# -*-coding:utf-8-*-

from flask import Flask

apps = Flask(__name__)

@apps.route('/')
# 捕捉url。此处为url无后缀
def hello_world():
    return '<h1> Love U Ma!</h1>'
    # 返回header，只能有一个header


if __name__ == '__main__':
    apps.debug = True;
    # 调试模式，开发使用

    # app.run()
    apps.run(host='0.0.0.0', port=1314);
    #此处为全IP，端口为1314