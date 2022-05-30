# coding: utf-8
""" 
@author: oldman
@file: test.py 
@time: 2022-05-13 14:40
"""

"""
给定升序数组 nums = [1,3,5,7,9], 查找目标值 target=10在数组中的索引位置，如果不存在返回-1

"""


def index_of_value(nums: list, target: int) -> int:
    for i in range(0, len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] > target:
            break
    return -1


def index_of_value_operate(nums: list, target: int) -> int:

    mid = len(nums) // 2
    if nums[0]<=target<nums[mid]:
        left = index_of_value_operate(nums[0:mid], target)
    if nums[mid]<target<=nums[mid]:
        right = index_of_value_operate(nums[mid:], target)



if __name__ == "__main__":
    nums = [1, 3, 4, 5, 6]
    taget = 3
    print(index_of_value(nums, 3))
    print(index_of_value(nums, 5))
    print(index_of_value(nums, 0))
