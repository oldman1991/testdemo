#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/10/16
"""
冒泡排序的实现
>>> a = [1,3,4,7,9,0,2,3,4,56]
>>> bubble_sort(a)
>>> print(a)
[0, 1, 2, 3, 3, 4, 4, 7, 9, 56]
"""


def bubble_sort(list_a):
    """
    冒泡排序
    :param list_a: 列表
    :return:
    """
    n = len(list_a)
    if n <= 1:
        return
    for i in range(0, n):
        # 提前退出冒泡循环的标志
        flag = False
        for j in range(0, n - i - 1):
            if list_a[j] > list_a[j + 1]:
                list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j]
                flag = True
        if not flag:
            break


a = [1, 3, 4, 7, 9, 0, 2, 3, 4, 56]
bubble_sort(a)
assert a == [0, 1, 2, 3, 3, 4, 4, 7, 9, 56]


def bubble_sort(list_a):
    if len(list_a) <= 1:
        return

    for i in range(len(list_a)):
        flag = False

        for j in range(0, n-i-1):
            if list_a[j]>list_a[j+1]:
                list_a[j], list_a[j+1] = list_a[j+1], list_a[j]
                flag = True
        if not flag:
            break
