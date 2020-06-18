# -*- coding:utf-8 -*-
'''
@Description: 使用docker创建一个flask应用
    https://zhuanlan.zhihu.com/p/71251233
@Author: lamborghini1993
@Date: 2019-07-04 17:31:36
@UpdateDate: 2019-07-04 21:00:39
'''

from flask import Flask

app = Flask(__name__)


@app.route("/")
def Index():
    return """
    <h1>Python Flask in Docker!</h1>
    <p>A sample web-app for running Flask inside Docker-1.</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
