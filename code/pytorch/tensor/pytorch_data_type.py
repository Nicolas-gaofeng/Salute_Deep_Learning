#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : pytorch_data_type.py
@author     : zgf
@brief      : pytorch 数据类型
@attention  : life is short,I need python
"""

import torch


# ===============================  type() ===============================
#
# flag = True
flag = False
if flag:
    a = torch.randn(2, 3)
    print(a.type())
    print(type(a))


# ===============================  isinstance() ===============================
#
# flag = True
flag = False
if flag:
    a = torch.randn(2, 3)
    print(isinstance(a, torch.FloatTensor))
    print(isinstance(a, torch.cuda.FloatTensor))
    a = a.cuda()
    print(isinstance(a, torch.cuda.FloatTensor))
