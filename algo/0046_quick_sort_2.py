#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/10/22
"""
快读排序的第二种实现方式
>>> a = [1, 3, 7, 5, 3, 2, 4]
>>> quick_sort(a, 0, len(a)-1)
>>> a
[1, 2, 3, 3, 4, 5, 7]
"""


def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)


def partition(arr, left, right):
    """
    找到基准位置，并返回
    :param arr:
    :param left:
    :param right:
    :return:
    """
    pivot_index = left
    pivot = arr[left]

    for i in range(left + 1, right + 1):
        if arr[i] < pivot:
            # 如果此处索引的值小于基准值, 基准值的位置后移一位
            # 并将后移一位的值和这个值交换, 让基准位置及之前的始终小于基准值
            pivot_index += 1
            if pivot_index != i:
                arr[pivot_index], arr[i] = arr[i], arr[pivot_index]

    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
    return pivot_index
