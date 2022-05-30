#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/11/7

"""
计数排序
计数排序只能用在数据范围不大的场景中，如果数据范围 k 比要排序的数据 n 大很多，就不适合用计数排序了。而且，计数排序只能给非负整数排序，如果要排序的数据是其他类型的，要将其在不改变相对大小的情况下，转化为非负整数。

>>> a = [1, 3, 5, 7, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 56, 7]
>>> counting_sort(a, len(a))
>>> a
[1, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 7, 7, 8, 9, 56]
"""


def counting_sort(arra, n):
    if n < 1:
        return
    max_value = arra[0]
    for item in arra:
        if item > max_value:
            max_value = item

    c = [0 for i in range(0, max_value + 1)]
    # 计算每个元素的个数放入到c中
    for item in arra:
        c[item] += 1

    # 依次累加
    for i in range(1, max_value + 1):
        c[i] += c[i - 1]

    # 临时数组 r, 存储排序之后的结果
    r = [0 for item in range(0, n)]

    # for i in range(n - 1, -1, -1):
    #     value = arra[i]
    #     index = c[value] - 1
    #     r[index] = value
    #     c[value] -= 1
    for i in range(0, n):
        value = arra[i]
        index = c[value] - 1
        r[index] = value
        c[value] -= 1
    for index, value in enumerate(r):
        arra[index] = r[index]


a = [1, 3, 5, 7, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 56, 7]
counting_sort(a, len(a))
print(a)
