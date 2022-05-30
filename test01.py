# coding: utf-8
""" 
@author: oldman
@file: test01.py 
@time: 2022-05-27 14:24
"""

"""
一维数组，返回第K大的数
排序，选择排序
"""


def merge(nums_left, nums_right):
    res = []
    n_left = 0
    n_right = 0

    while n_left < len(nums_left) and n_right < len(nums_right):
        if nums_left[n_left] >= nums_right[n_right]:
            res.append(nums_left[n_left])
            n_left += 1
        else:
            res.append(nums_right[n_right])
            n_right += 1
    res.extend(nums_left[n_left:])
    res.extend(nums_right[n_right:])
    return res


def merge_sort(nums, left, right):
    mid = (right + left) // 2

    if left == mid:
        return [nums[left]]
    if right == mid:
        return [nums[right]]

    left = merge_sort(nums, )

    right = merge_sort(nums[mid:])

    return merge(left, right)


num_a = [1,3,4,2,7,6]
print(merge_sort(num_a,0, len(num_a)-1))




