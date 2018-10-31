from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URL'] = DB_URI
# app.config.from_object('consts')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:20Miqianlan@47.106.99.78:3306/r'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

# print(db)

# #app程序上下文，会在实例调用之后触发
with app.app_context():
    db.drop_all()
    db.create_all()


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    #backref 相当于双向关联关系，backref关键字单独的用在一边和在关系两边使用back_populates关键字,效果是完全等价的
    users = db.relationship('User', backref='role')

#重新定义输出格式
def __repr__(self):
    return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

def __repr__(self):
    return '<User %r>' % self.username

#确认是运行__main__函数才run，而不是导入的时候,或者父级脚本执行,启动后会进入轮询直到停止
if __name__ == '__main__':
    app.debug = True;
    # 调试模式，开发使用
    # app.run()
    app.run(host = '0.0.0.0', port = 12333);
    #此处为全IP，端口为1314,®外网可以访问到