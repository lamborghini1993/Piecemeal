# -*- coding:utf-8 -*-
'''
@Description: 
    1. 测试pylint是否可以检测外部文件
    2. 测试是否可以跳转到外部文件
    外部文件为 ExtraPath/extrafile
@Author: lamborghini1993
@Date: 2019-05-10 16:26:11
@UpdateDate: 2019-05-10 16:40:22
'''

from PyQt5 import QtCore

import extrafile

extrafile.Test()
print(QtCore.Qt.black)
