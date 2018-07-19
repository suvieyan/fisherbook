from flask import Flask,make_response

app = Flask(__name__)
app.config.from_object('config')  # 导入配置文件的路径

@app.route('/book/search/')
def search():
    """
    检索的数据，不需要区分关键字和isbn搜索的区分
        q:普通+isbn
            isbn，不保留
        page
            start
            count

    :return:
    """
    pass


if __name__ == '__main__':
    # 生产环境：nginx+uwsigi执行
    app.run(host='192.168.43.27', debug=app.config['DEBUG'], port=81)

