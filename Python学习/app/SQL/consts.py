
#python3 , sql config

HOSTNAME = 'localhost'
DATABASE = 'rootFlask'
USERNAME = 'web'
PASSWORD = 'web'
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,DATABASE)
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
DEBUG = True


DB_URI = 'mysql://root:20Miqianlan@47.106.99.78:3306/r'
SQLALCHEMY_TRACK_MODIFICATIONS = False