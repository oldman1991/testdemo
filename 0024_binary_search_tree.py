# coding=utf-8
# create by oldman at 2018/6/8
"""
二叉查找树
二叉查找树（Binary Search Tree），又称为二叉搜索树、二叉排序树。其或者是一棵空树；或者是具有以下性质的二叉树：

若左子树不空，则左子树上所有结点的值均小于或等于它的根结点的值
若右子树不空，则右子树上所有结点的值均大于或等于它的根结点的值
左、右子树也分别为二叉排序树

"""
from binarytree.node import Node


class BinarySearchTree(object):
    """
    二叉查找树
    """
    def __init__(self, nodeList):
        self.root = Node(nodeList[0])
        for data in nodeList[1:]:
            self.insert(data)

    #搜索
    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node,data)
        else:
            return self.search(node.rchild, node, data)

    # 插入
    def insert(self, data):
        """
        :param data:
        """
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
            if



