# 配置文件当中的值最好大写，类似于全局变量
# 数据库、密码、
# 生产环境的相关配置

DEBUG = False

# cymysql:引擎
# sqlalchemy 支持分布式的数据库

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost:3306/fisher?charset=utf8'

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True


