# coding=utf-8
# create by oldman at 2018/6/22
"""
元组的相对不可变性
"""
a = [[3] * 3] * 3
a[0][0] = 1
a

b = (1, 2, [30, 40])
b[2] += [50, 60]
