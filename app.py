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
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return "Welcome to My Watchlist!"
