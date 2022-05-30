# coding=utf-8
# create by oldman at 2018/4/23

"""
反转一个单链表。

进阶:
链表可以迭代或递归地反转。你能否两个都实现一遍？
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        last_node = head
        next_node = head
        while (last_node.next):
            cur = last_node.next
            cur_next = cur.next
            cur.next = next_node
            last_node.next = cur_next
            next_node = cur
        return next_node


"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        num = 1
        # 找到要翻转部分的开始
        while num != m:
            pre = pre.next
            num += 1
        # gap为循环的次数
        gap = n - m + 1
        # 第二部分
        next_part = pre.next
        # 设置第一部分的尾节点，目的在于最后的合并
        tail = next_part
        pre.next = None
        while gap != 0:
            cur = next_part
            next_part = next_part.next
            temp = pre.next
            pre.next = cur
            cur.next = temp
            gap -= 1
        # 两部分合并
        tail.next = next_part
        return dummy.next


# 翻转链表
def reverseList(head):
    cur, pre = head, None
    while cur:
        cur.next, pre, cur = pre, cur, cur.next
    return pre
