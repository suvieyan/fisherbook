"""
 Created by yan on 2018/8/30 15:41
 验证web的book的参数
 使用wtforms做验证器的思想需要学习下
"""

from wtforms import Form,StringField,IntegerField
from wtforms.validators import Length,NumberRange,DataRequired

__author__ = 'yan'

class SearchForm(Form):
    q = StringField(validators=[DataRequired(message='q长度不能为空'),Length(min=1,max=30,message='长度为1-30')])
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)


