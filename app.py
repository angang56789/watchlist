#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2022-10-13 16:52
@Site : 
@Author : 
@Project：watchlist
@File : app.py
@Version：V 0.1
@Software: PyCharm
@desc :
"""
from flask import Flask,url_for
from markupsafe import escape

app = Flask(__name__)
@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='bob'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'test page'
