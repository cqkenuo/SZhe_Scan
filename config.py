import os
import redis
from rq import Queue
import rqsettings

'''
配置文件：
    debug=true
    secret_key,session中的24位随机盐值
    MySQL数据库配置
    数据库名为SZheScan
        python3:https://blog.csdn.net/qq562029186/article/details/81325074
'''
# DEBUG = True
DEBUG = False
SECRET_KEY = os.urandom(24)

HOSTNAME='mysql'
# HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'SZheScan'
USERNAME = 'root'
PASSWORD = 'root'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/tushare?charset=utf8'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT,
                                                                               DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False

HOST = 'redis'
# HOST = '127.0.0.1'
redisPool = redis.ConnectionPool(host=HOST, port=6379, db=0, decode_responses=True)
db = redis.Redis(host=rqsettings.REDIS_HOST, port=rqsettings.REDIS_PORT, db=rqsettings.REDIS_DB, decode_responses=True)
queue = Queue(connection=db)
