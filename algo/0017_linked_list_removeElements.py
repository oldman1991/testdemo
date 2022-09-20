# coding=utf-8
# create by oldman at 2018/3/28
"""
删除链表中等于给定值 val 的所有元素。

示例
给定: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
返回: 1 --> 2 --> 3 --> 4 --> 5
"""


class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def removeElements(head, val):
    """

    :param head: listNode
    :param val: int
    :return: listNode
    """
    dump = ListNode(-1)
    dump.next = head
    cur = head
    pre = dump
    while cur:
        if cur.value == val:
            pre.next = cur.next
        else:
            pre = pre.next
        cur = cur.next

    return dump.next
