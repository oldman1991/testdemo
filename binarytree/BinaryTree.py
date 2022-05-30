# coding=utf-8
# create by oldman at 2018/5/23


class TreeNode(object):
    """
    二叉树
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""


class Solution(object):
    def levelOrder(self, root):
        """

        :param root:  TreeNode
        :return: List[list[int]]
        """
        res = []
        if not root:
            return res
        q = [root]
        while len(q) != 0:
            temp = []
            length = len(q)
            for i in range(length):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                temp.append(q.val)
            res.append(temp)
        return res


"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""


class Solution(object):
    def levelOrder(self, root):
        """

        :param root:  TreeNode
        :return: List[list[int]]
        """
        res = []
        if not root:
            return res
        q = [root]
        while len(q) != 0:
            temp = []
            length = len(q)
            for i in range(length):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                temp.append(q.val)
            res.insert(0, temp)
        return res


"""
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

示例 1:

输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
注意：

 1.节点值的范围在32位有符号整数范围内。
"""


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        if root is None:
            return res
        q = [root]
        while len(q) != 0:
            sum = 0
            length = len(q)
            for i in range(length):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                sum += node.val
            res.append(sum / (length * 1.0))
        return res


"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = [root]
        deep = 0
        while len(q) != 0:
            deep += 1
            length = len(q)
            for i in range(length):
                node = q.pop(0)
                if not (node.left or node.right):
                    return deep
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
