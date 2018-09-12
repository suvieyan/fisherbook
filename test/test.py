"""
 Created by yan on 2018/8/30 17:39
"""
__author__ = 'yan'

from flask import Flask,current_app,request,Request

app = Flask(__name__)

a = current_app
print(current_app)  # RuntimeError: Working outside of application context.

