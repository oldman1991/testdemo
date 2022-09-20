#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/8/28
"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

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
import collections


def  levelOrder(root):
    if not root :
        return []
    result = []
    queue = collections.deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
    return result


def levelOrder1(root):
    """
    递归实现
    :param root:
    :return:
    """
    levels = []
    if not root:
        return levels

    def helper(node, level):
        # strat the current level
        if len(levels) == level:
            levels.append([])

        # append the current node value
        levels[level].append(node.val)

        if node.left:
            helper(node.left, level+1)
        if node.right:
            helper(node.right, level+1)

    helper(root, 0)
