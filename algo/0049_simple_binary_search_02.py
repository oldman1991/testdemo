#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/11/1
"""
>>> a = [1,2,3,4,4,5,6,7,8]
>>> value = 4
>>> bsearch01(a, value)
3
>>> bsearch02(a, value)
4
>>> bsearch03(a, value)
3
>>> bsearch04(a, value)
4
"""


def bsearch01(arra, value):
    """
    查找第一个值等于给定值的元素
    :return:
    """
    high = len(arra)
    low = 0
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arra[mid] > value:
            high = mid - 1
        elif arra[mid] < value:
            low = mid + 1
        else:
            if mid == 0 or arra[mid - 1] != value:
                return mid
            else:
                high = mid - 1

    return -1


def bsearch02(arra, value):
    """
    查找最后一个值等于给定的值的元素
    :param arra:
    :param value:
    :return:
    """
    low = 0
    high = len(arra)
    n = high + 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arra[mid] > value:
            high = mid - 1
        elif arra[mid] < value:
            low = mid + 1
        else:
            if mid == n - 1 or arra[mid + 1] != value:
                return mid
            else:
                low = mid + 1
    return -1


def bsearch03(arra, value):
    """
    查找第一个大于等于给定值的元素
    :param arra:
    :param value:
    :return:
    """
    low = 0
    high = len(arra)
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arra[mid] >= value:
            if mid == 0 or arra[mid - 1] < value:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    return -1


def bsearch04(arra, value):
    """
    查找最后一个小于等于给定值的元素
    :param arra:
    :param value:
    :return:
    """
    low = 0
    high = len(arra)
    n = high + 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arra[mid] <= value:
            if mid == n - 1 or arra[mid + 1] > value:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1
    return -1
