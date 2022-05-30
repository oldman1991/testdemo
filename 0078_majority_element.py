#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/8/28
"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

"""


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dict_nums = {}
    for i in nums:
        dict_nums[i] = dict_nums.get(i, 0) + 1
    for key, value in dict_nums.items():
        if value > len(nums) / 2:
            return key
    return None