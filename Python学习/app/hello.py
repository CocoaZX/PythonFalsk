
#flaskwtf验证用户数据

from flask_wtf import Form
from flask import Flask
from wtforms import StringField,SubmitField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'it\'s a long string'


class NameForm(Form):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')

#确认是运行__main__函数才run，而不是导入的时候,或者父级脚本执行,启动后会进入轮询直到停止
if __name__ == '__main__':
    app.debug = True
    # 调试模式，开发使用
    # app.run()
    app.run(host='0.0.0.0', port=12333);



