# coding=utf-8
# create by oldman at 2018/4/11
"""
给出一个链表，一次翻转 k 个指针节点，并返回修改后的链表。

k 是一个正整数，并且小于等于链表的长度。如果指针节点的数量不是 k 的整数倍，那么最后剩余的节点应当保持原来的样子。

你不应该改变节点的值，只有节点位置本身可能会改变。

题目应当保证，仅使用恒定的内存。

例如，

给定这个链表：1->2->3->4->5

当 k = 2时，应当返回: 2->1->4->3->5

当 k = 3时，应当返回: 3->2->1->4->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseOneGroup(pre_node, next_node):
    last_node = pre_node.next
    cur_node = last_node.next
    while cur_node != next_node:
        last_node.next = cur_node.next
        cur_node.next = pre_node.next
        pre_node.next = cur_node
        cur_node = last_node.next

    return last_node


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1 or not head:
            return head
        dump = ListNode(-1)
        dump.next = head
        pre = dump
        cur = head
        i = 0
        while cur:
            i += 1
            if i % k == 0:
                pre = reverseOneGroup(pre, cur.next)
                cur = pre.next
            else:
                cur = cur.next

        return dump.next
