from flask import Flask,make_response

from helper import is_isbn_or_key

app = Flask(__name__)
app.config.from_object('config')  # 导入配置文件的路径


# q和page是参数
@app.route('/book/search/<q>/<page>')
def search(q,page):
    """
    :param q: 关键字还是isbn
    :param page: 分页相关
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    pass


if __name__ == '__main__':
    # 生产环境：nginx+uwsigi执行
    app.run(host='192.168.43.27', debug=app.config['DEBUG'], port=81)

