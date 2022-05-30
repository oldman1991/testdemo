#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/10/16
"""
插入排序
>>> a = [1,3,4,7,9,0,2,3,4,56]
>>> insert_sort(a)
>>> print(a)
[0, 1, 2, 3, 3, 4, 4, 7, 9, 56]
"""


def insert_sort(list_a):
    """
    插入排序
    :param list_a:
    :return:
    """
    n = len(list_a)
    if n <= 1:
        return
    for i in range(1, n):
        for j in range(i, 0, -1):
            if list_a[j - 1] > list_a[j]:
                list_a[j - 1], list_a[j] = list_a[j], list_a[j - 1]
            else:
                break


a = [1, 3, 4, 7, 9, 0, 2, 3, 4, 56]
insert_sort(a)
assert a == [0, 1, 2, 3, 3, 4, 4, 7, 9, 56]
print(a)
