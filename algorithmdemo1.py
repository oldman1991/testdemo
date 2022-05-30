# coding=utf-8


# coding=utf-8

"""
  *
  * 283. Move Zeroes My Submissions QuestionEditorial Solution

  * Given an array nums, write a function to move all 0's to the end of it
  * while maintaining the relative order of the non-zero elements.

  * For example, given nums = [0, 1, 0, 3, 12],
  * after calling your function, nums should be [1, 3, 12, 0, 0].
  *
  *
  * 0,1,0,3,12 0 ... 4
  *
  *             1st 0's index
  * 0,1,0,3,12  0
  * 1,0,0,3,12  1
  * 1,0,0,3,12  1
  * 1,3,0,0,12  2
  * 1,3,12,0,0  3
  *
  * in place O(1) space complexity
  * O(n) time complexity
  *
  * 1，0，3，4，0，8    1
  * 1, 3, 0 ,4, 0, 8   2
  * 1,3,4,0,0,8   3
"""
import gc


def moveZeros(target):
    indexofzero = []
    for index, value in enumerate(target):
        if value == 0:
            indexofzero.append(index)
        elif len(indexofzero) > 0:
            target[index] = 0
            target[indexofzero[0]] = value
            del indexofzero[0]
            indexofzero.append(index)
    print(target)
    gc.collect()

arr = [1, 0, 0, 3, 5, 6, 0, 7, 0, 9, 1, 3, 4]
moveZeros(arr)
