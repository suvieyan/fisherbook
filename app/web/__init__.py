"""
 Created by yan on 2018/8/30 14:53
 蓝图的相关初始化工作
"""

__author__ = 'yan'

from app.web.blueprint import web

# 必须首先导入执行以下，否则没有引入，会有循环导入
from app.web import book

