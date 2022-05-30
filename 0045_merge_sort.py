#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/10/22
"""
归并排序
>>> seq = [5, 3, 0, 6, 4, 1]
>>> merge_sort(seq)
[0, 1, 3, 4, 5, 6]
"""


def merge_sort(seq):
    if len(seq) <= 1:
        return seq

    mid = len(seq) // 2

    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(seq):
    if len(seq)<=1:
        return seq

    mid = len(seq)//2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i<len(left) and j<len(right):
        if left[i]<= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
