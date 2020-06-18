# -*- coding:utf-8 -*-
'''
@Description: docker实战flask
@Author: lamborghini1993
@Date: 2019-08-23 14:25:40
@UpdateDate: 2019-08-23 14:26:31
'''

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "hello docker public attention:idig88"


if __name__ == '__main__':
    app.run(port=8888)
