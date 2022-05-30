# coding=utf-8
# create by oldman at 2018/1/17
"""
排序算法之侏儒算法
"""


def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i - 1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i - 1] = seq[i - 1], seq[i]
            i -= 1


"""
排序算法之归并算法
"""

# def mergesort(seq):
#     mid = len(seq)/2
#     lft, rgt = seq[:mid], seq[mid:]
#     if len()