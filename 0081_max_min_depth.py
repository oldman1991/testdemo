#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/8/29
"""
二叉树的最大最小深度

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。




给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

"""
import collections


def maxDepth(root):
    if not root:
        return 0
    return 1+ max(maxDepth(root.left), maxDepth(root.right))


def maxDepth1(root):
    if not root:
        return 0
    q = collections.deque()
    q.append(root
    deepth = 0
    while q:
        deepth+=1
        length=len(q)
        for _ in range(length):
            node = q.popleft()
            if node.left:q.append(node.left)
            if node.right:q.append(node.right)

    return deepth

def minDepth(root):
    if not root:
        return 0
    if not root.left:
        return 1+minDepth(root.right)

    if not root.right:
        return 1+minDepth(root.left)

    return min(minDepth(root.left), minDepth(root.right)) + 1


def minDepth1(root):
    if not root:
        return 0
    q = collections.deque()
    q.append(root)
    deep = 0
    while q:
        deep+=1
        length = len(q)
        for _ in range(length):
            node = q.popleft()
            if not(node.left or node.right):
                return deep
            else:
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)

