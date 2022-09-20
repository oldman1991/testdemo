#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/3/26
"""
>>>a = [1, -1, 2, 3, 7, 3, 4, 2]
>>>maxSlideWindow1(a, 3)
>>>[2, 3, 7, 7, 7, 4]
"""


def maxSlideWindow1(nums, k):
    if not nums:
        return []
    windows, res = [], []
    for i, x in enumerate(nums):
        if i >= k and windows[0] <= i - k:
            windows.pop(0)
        while windows and nums[windows[-1]] <= x:
            windows.pop()
        windows.append(i)
        if i >= k - 1:
            res.append(nums[windows[0]])
    return res


a = [1, -1, 2, 3, 7, 3, 4, 2]
print(maxSlideWindow1(a, 3))
