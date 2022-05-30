# coding: utf-8
""" 
@author: oldman
@file: depth.py 
@time: 2022-05-12 14:22
"""


def max_depth(root):
    """
    二叉树的最大深度
    :param root:
    :return:
    """

    if root is None:
        return 0
    else:
        left = max_depth(root.left)
        right = max_depth(root.right)
        return max(left, right) + 1


class Tree():
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


if __name__ == "__main__":
    a = Tree(5)
    b = Tree(6)
    c = Tree(7)
    a.left = b
    b.left = c
    print(max_depth(a))
