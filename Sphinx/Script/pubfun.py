# -*- coding:utf-8 -*-
"""
公用方法
"""

__author__ = "lamborghini1993"
__date__ = "2020-01-16 17:07:35"


import enum
import time


def GetRunTime(func):
    """获取执行func的时间
    
    Args:
        func (function): 执行的函数
    
    Returns:
        Any: 返回的结果
    """
    def _run(*args):
        """func闭包
        
        Returns:
            [Any]: 结果
        """
        begin = time.time()
        result = func(*args)
        print("run %s s" % time.time() - begin)
        return result
    return _run


class Enum(enum.Enum):
    """枚举"""
    A = 1   #: A
    B = 2   #: B


class Foo:
    """Docstring for class Foo."""

    #: Doc comment for class attribute Foo.bar.
    #: It can have multiple lines.
    bar = 1

    flox = 1.5   #: Doc comment for Foo.flox. One line only.

    baz = 2
    """Docstring for class attribute Foo.baz."""

    def __init__(self):
        #: Doc comment for instance attribute qux.
        self.qux = 3

        self.spam = 4
        """Docstring for instance attribute spam."""
