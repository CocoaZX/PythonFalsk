import pymysql

#手写SQL方法
# #打开数据库
db = pymysql.connect(host="47.106.99.78",user="root",password="20Miqianlan",db="mysql",port=3306)
#
# #获取操作游标
# cur = db.cursor()

#with语句会自动判断语句有无错误，有错误就回滚，没有错误就事务提交。不需要自己写trycache
with db as cur:
    cur.execute('drop table if exists users')
    cur.execute('create table users(Id INT PRIMARY KEY AUTO_INCREMENT ,Name VARCHAR(25))')#此处自增提示补全没有下划线，可能pymysql和mysql字段不完全对应，略坑
    #增
    cur.execute('insert into users(NAME) values ("zhuzhu")')
    #查
    cur.execute('select * from users')
    rows = cur.fetchall()

    for row in rows:
        print(row)
    #改,注意直接改是异步
    # cur = db.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('update users set NAME = %s where Id = %s',('gouzi','1'))
    cur.execute('select * from users')
    rows = cur.fetchall()
    for row in row:
        print(row)

# sql_insert = """insert into user(id,username,password) values(4,'liu','1234')"""
#
# try:
#     cur.execute(sql_insert)
#     # 提交
#     db.commit()
# except Exception as e:
#     # 错误回滚
#     db.rollback()
# finally:
#     db.close()

