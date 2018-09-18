"""
 Created by yan on 2018/8/30 14:52
"""
from flask import Flask
from app.models.book import db

__author__ = 'yan'

def create_app():
    # alt+enter 快捷导入
    app = Flask(__name__,static_folder='view_models/statics')
    print('__name__',__name__)  # app
    # 导入配置文件的路径
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    # 一个经典问题：No application found. Either work inside a view function or push
    # 方法一
    db.create_all(app=app)
    # 方法二，RPG代入感，移情，认同感，学习看源代码去学习
    # with app.context:
    #     db.create_all()
    # 方法三,在定义的时候，就直接引入这个核心对象
    # db = SQLAlchemy(app)

    return app




def register_blueprint(app):
    from app.web.book import web
    # 注册蓝图
    app.register_blueprint(web)
