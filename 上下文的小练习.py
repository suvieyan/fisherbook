"""
 Created by yan on 2018/9/29 15:29
"""
__author__ = 'yan'
from contextlib import contextmanager

def start():
    for i in range(5):
        print(i,end='')

class MyManager():
    @contextmanager
    def test(self):
        print('一些func')
        yield
        print('结束func')

manager = MyManager()
with manager.test():
    print('Hello World')