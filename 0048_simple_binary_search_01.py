#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/10/24
"""
>>> a = [1, 2,3 ,4, 5, 6, 7, 8]
>>> simple_binary_search(a, 8, 4)
3
>>> simple_binary_search_internally(a,0,7,4)
3
"""


def simple_binary_search(arr, n, value):
    """
    简单的二分查找
    :param arr:
    :param n:
    :param value:
    :return:
    """
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def simple_binary_search_internally(arr, low, high, value):
    """
    简单二分查找的递归实现
    :param arr: 有序数组
    :param low:
    :param high:
    :param value: 查找值
    :return:
    """
    if low > high:
        return -1
    mid = low + ((high - low) >> 1)
    if arr[mid] == value:
        return mid
    if arr[mid] < value:
        return simple_binary_search_internally(arr, mid+1, high, value)
    else:
        return simple_binary_search_internally()
