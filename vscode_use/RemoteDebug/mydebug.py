# -*- coding:utf-8 -*-
'''
@Description: 远程调试样例
@Author: lamborghini1993
@Date: 2019-04-08 22:26:32
@UpdateDate: 2019-05-10 16:07:15
'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--debug", type=int, default=0, help="是否启用ptvsd调试")
args = parser.parse_args()

if args.debug:  # 第一种方式
    import ptvsd
    ptvsd.enable_attach(address=('0.0.0.0', 3000), redirect_output=True)
    print("ptvsd has started, ready to attach the debugger")
    ptvsd.wait_for_attach()

# if args.debug:  # 第二种方式
#     import pydev_startup

num = 0
for x in range(10):
    num += x
    print(num)
