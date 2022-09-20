#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/10/22
"""
O(N)寻找第K大的数
>>> a = [1,3,7,6,5,4,6,8,9]
>>> find_k_th(a, 4, 0, len(a)-1)
6
"""


def find_k_th(arr, k, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        if pivot_index == k:
            return arr[pivot_index]
        if pivot_index < k:
            return find_k_th(arr, k, pivot_index + 1, right)
        else:
            return find_k_th(arr, k, left, pivot_index - 1)


def partition(arr, left, right):
    """
    使用快排的思想找到标志位
    :param arr:
    :param left:
    :param right:
    :return:
    """
    pivot = arr[left]
    pivot_index = left
    for i in range(left + 1, right + 1):
        if arr[i] < pivot:
            pivot_index += 1
            if pivot_index != i:
                arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
    return pivot_index


a = [1, 3, 7, 6, 5, 4, 6, 8, 9]
b = find_k_th(a, 4, 0, len(a) - 1)
print(b)
