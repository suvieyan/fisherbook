from flask import Flask

app = Flask(__name__)
print(1,id(app))
app.config.from_object('config')  # 导入配置文件的路径

from app.web import book

if __name__ == '__main__':
    # 生产环境：nginx+uwsigi执行
    print(2,id(app))
    app.run(debug=app.config['DEBUG'], port=81)

