from SQL.ext import db

class User(db.Model):
    __tablename__ = 'r'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))

    def __init__(self,name):
        self.name = name

    #重构输出控制台方法
    def __repr__(self):
        return '<User %r>' % self.name


