from sqlalchemy import  create_engine,Column,Integer,String,Sequence
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy import  and_,or_
from sqlalchemy.orm import sessionmakers


eng = create_engine('mysql://root:20Miqianlan@47106.99.78:3306/r')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,Sequence('user_id_seq'),primary_key=True,autoincrement=True)
    name = Column(String(50))

Base.metadata.drop_all()
