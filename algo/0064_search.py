#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/5/29
"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""
"""
题目中说明要用 O(log n) 能想到就是二分法!

思路一：
整体思路：先用二分法找出最小值，也是那个分割点,例如 [4,5,6,7,0,1,2]，我们找出数字 0；

接下来判断 target 是在分割点的左边还是右边;

最后再使用一次二分法找出 target 的位置. 所以时间复杂度为：O(logn)O(logn)

只有一个难点，那就是如何通过二分法找出那个分割点呢？

就是和它的右端点比较判断，直接看代码吧！

思路二：
直接使用二分法，判断那个二分点,有几种可能性

直接等于target

在左半边的递增区域

a. target 在 left 和 mid 之间

b. 不在之间

在右半边的递增区域

a. target 在 mid 和 right 之间

b. 不在之间

"""


def search(nums, target) -> int:
    n = len(nums)
    if n == 0:
        return -1
    left = 0
    right = n - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    # print(left,right)
    return left if nums[left] == target else -1


class Solution:
    def search(self, nums, target) -> int:
        if not nums: return -1
        n = len(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        t = left
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            realmid = (mid + t) % n
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
