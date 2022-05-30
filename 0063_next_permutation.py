#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/5/27
"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


"""


def reverse(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


def nextPermutation(nums):
    firstIndex = -1
    n = len(nums)

    for i in range(n-2):
        if nums[i] < nums[i+1]:
            firstIndex = i
            break
    if firstIndex == -1:
        reverse(nums, 0, n-1)
        return
    secondIndex = -1
    for i in range(n-1, firstIndex, -1):
        if nums[i] > nums[firstIndex]:
            secondIndex = i
            break
    nums[firstIndex], nums[secondIndex] = nums[secondIndex], nums[firstIndex]
    reverse(nums,firstIndex+1, n-1)
