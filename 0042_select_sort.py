#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/10/16
"""
选择排序
>>> a = [1,3,4,7,9,0,2,3,4,56]
>>> select_sort(a)
>>> print(a)
[0, 1, 2, 3, 3, 4, 4, 7, 9, 56]
"""


def select_sort(list_a):
    """
    选择排序
    :param list_a:
    :return:
    """
    n = len(list_a)
    for i in range(0, n):
        min_num = i
        for j in range(i + 1, n):
            if list_a[min_num] > list_a[j]:
                min_num = j
        list_a[min_num], list_a[i] = list_a[i], list_a[min_num]


a = [1, 3, 4, 7, 9, 0, 2, 3, 4, 56]
select_sort(a)
assert a == [0, 1, 2, 3, 3, 4, 4, 7, 9, 56]
print(a)