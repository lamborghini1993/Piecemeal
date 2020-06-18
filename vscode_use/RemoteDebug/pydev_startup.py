# -*- coding:utf-8 -*-
'''
@Description: ptvsd调试
@Author: lamborghini1993
@Date: 2019-04-08 23:15:33
@UpdateDate: 2019-04-09 00:20:39
'''

import ptvsd

# Modify the port number as desired; you're debugging locally so the values don't matter.
# However, be sure the port is not blocked on your computer.
ptvsd.enable_attach(address=('0.0.0.0', 3000), redirect_output=True)

# The debug server has started and you can now use VS Code to attach to the application for debugging
print("ptvsd has started, ready to attach the debugger")
ptvsd.wait_for_attach()
