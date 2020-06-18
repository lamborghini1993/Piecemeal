# -*- coding:utf-8 -*-
'''
@Description: 测试docker-compnse
@Author: lamborghini1993
@Date: 2019-08-22 16:06:12
@UpdateDate: 2019-08-23 17:22:00
'''

import time

from flask import Flask

import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
