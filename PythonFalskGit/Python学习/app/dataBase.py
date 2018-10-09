
import flask
import flask_sqlalchemy
from flask_security import  RoleMixin

# class Product(db.Model):
#     __tablename__ = 'product'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     file_name = db.Column(db.String)
#     version = db.Column(db.String)
#     is_active = db.Column(db.Boolean, default=True)
#     price = db.Column(db.Float)
#
#
# class Purchase(db.Model):
#     __tablename__ = 'purchase'
#     uuid = db.Column(db.String, primary_key=True)
#     email = db.Column(db.String)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
#     product = db.relationship(Product)
#     downloads_left = db.Column(db.Integer, default=5)

class Role(db.Model,RoleMixin):
    print(1)