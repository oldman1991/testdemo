#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/8/28


class Traversal():
    """
    前序(Pre-order):根-左-右
    中序(In-order):左-根-右
    后序(Pre-order):左-右-根
    """
    def __init__(self):
        self.traverse_path = []

    def preorder(self, root):
        if root:
            self.traverse_path.append(root.value)
            self.preorder(root.left)
            self.preorder(root.right)


    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.traverse_path.append(root.value)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.traverse_path.append(root.value)


