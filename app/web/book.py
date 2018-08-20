from flask import jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook

from fisher import app
print(3,id(app))

# q和page是参数
@app.route('/book/search/<q>/<page>')
def search(q,page):
    """
    :param q: 关键字还是isbn
    :param page: 分页相关
    :return:
    """

    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        # 第一次的亲密接触api:http://127.0.0.1:81/book/search/9787501524044/1
        # 如果没有导入，快捷导入：alt+enter
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    # 主要是这种返回的思路，带上响应头
    # return json.dumps(result,ensure_ascii=False),200,{'content-type':'application/json'}
    # API：数据用json格式返回给客户端
    return jsonify(result)