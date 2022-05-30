#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/11/20


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, tree):
        self.tree = tree

    def find(self, data):
        p = self.tree
        while p is not None:
            if data < p.data:
                p = p.left
            elif data > p.data:
                p = p.right
            else:
                return p
        return None

    def insert(self, data):
        if self.tree is None:
            return Node(data)
        p = self.tree
        while p is not None:
            if data > p.data:
                if p.right is None:
                    p.right = Node(data)
                    return
                p = p.right
            else:
                if p.left is None:
                    p.left = Node(data)
                    return
                p = p.left

    def delete(self, data):
        p = self.tree  # 指向要删除的节点，初始化指向根节点
        pp = None  # pp记录的是p的父节点
        while p is not None and p.data != data:
            pp = p
            if p.data > data:
                p = p.left
            else:
                p = p.right
        if p is None:
            return
        # 要删除的节点有两个子节点
        if p.left is not None and p.right is not Node:  # 查找右子数中最小的节点
            pre = p.right
            if pre.left is None:
                p.data = pre.data
                p.right = pre.right
            else:
                next = pre.left
                while next.left is not None:
                    pre = next
                    next = next.left
                p.data = next.data
                pre.left = next.right
        # 删除节点是叶子节点或者仅有一个子节点
        if p.left is not None:
            child = p.left
        elif p.right is not None:
            child = p.right
        else:
            child = None

        if pp is None:  # 删除的是根节点
            self.tree = child
        elif pp.left == p:
            pp.left = child
        else:
            pp.right = child
