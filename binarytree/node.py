# coding=utf-8
# create by oldman at 2018/6/8
"""
树的节点
"""


class Node(object):
    """
    树的节点类
    """

    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


def testfunc(a):
    print(a)