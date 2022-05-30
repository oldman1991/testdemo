#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/8/28


"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
"""

def myPow(x,n):
    if not n:
        return 1
    if n< 0 :
        return 1/myPow(x,-n)
    if n%2:
        return x*(myPow(x,n-1))
    return myPow(x*x,n/2)


def myPow2(x, n):
    """
    非递归实现
    :param x:
    :param n:
    :return:
    """
    if n<0:
        x = 1/x
        n = -n
    pows = 1
    while n:
        if n & 1:
            pows *=x
        x *=x
        n >>= 1
    return pows