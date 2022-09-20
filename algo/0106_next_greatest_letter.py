# coding: utf-8
""" 
@author: oldman
@file: 0106_next_greatest_letter.py 
@time: 2022-05-30 15:31
"""
"""
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。

在比较时，字母是依序循环出现的。举个例子：

如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'
 

示例 1：

输入: letters = ["c", "f", "j"]，target = "a"
输出: "c"
示例 2:

输入: letters = ["c","f","j"], target = "c"
输出: "f"
示例 3:

输入: letters = ["c","f","j"], target = "d"
输出: "f"
 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-smallest-letter-greater-than-target
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def nextGreatestLetter(self, letters, target):

        l , r = 0 , len(letters)-1
        while l <= r:
            mid = (l + r)//2
            if letters[mid] > target:
                res = letters[mid]
                r = mid - 1
            else:
                l = mid + 1
        return res

