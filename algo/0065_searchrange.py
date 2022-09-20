#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/5/29
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

"""


def searchRange(nums, target):
    res = [-1, -1]
    if not nums: return res
    n = len(nums)
    if nums[0] > target or nums[n - 1] < target:
        return res
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] == target:
            left, right = mid, mid
            while left > 0 and nums[left - 1] == nums[left]:
                left -= 1
            while right < n - 1 and nums[right + 1] == nums[right]:
                right += 1
            res[0] = left
            res[1] = right
            break
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return res


nums = [1, 2, 3, 3, 3, 4, 5]
print(searchRange(nums, 3))
