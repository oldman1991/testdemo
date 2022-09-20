# coding: utf-8
"""
@author: oldman
@file: test.py
@time: 2022-05-13 14:40
"""

"""
给定升序数组 nums = [1,3,5,7,9], 查找目标值 target=10在数组中的索引位置，如果不存在返回-1

"""


# def index_of_value(nums: list, target: int) -> int:
#     for i in range(0, len(nums)):
#         if nums[i] == target:
#             return i
#         elif nums[i] > target:
#             break
#     return -1
#
#
# def index_of_value_operate(nums: list, target: int) -> int:
#
#     mid = len(nums) // 2
#     if nums[0]<=target<nums[mid]:
#         left = index_of_value_operate(nums[0:mid], target)
#     if nums[mid]<target<=nums[mid]:
#         right = index_of_value_operate(nums[mid:], target)
#
#
#
# if __name__ == "__main__":
#     nums = [1, 3, 4, 5, 6]
#     taget = 3
#     print(index_of_value(nums, 3))
#     print(index_of_value(nums, 5))
#     print(index_of_value(nums, 0))

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res


作者：jyd
链接：https://leetcode.cn/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/solution/mian-shi-ti-54-er-cha-sou-suo-shu-de-di-k-da-jie-d/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


作者：jyd
链接：https: // leetcode.cn / problems / er - cha - sou - suo - shu - de - di - kda - jie - dian - lcof / solution / mian - shi - ti - 54 - er - cha - sou - suo - shu - de - di - k - da - jie - d /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

作者：jyd
链接：https://leetcode.cn/problems/ping-heng-er-cha-shu-lcof/solution/mian-shi-ti-55-ii-ping-heng-er-cha-shu-cong-di-zhi/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
