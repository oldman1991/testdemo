# coding=utf-8
# create by oldman at 2018/3/30
"""

给定两个非空链表来代表两个非负数，位数按照逆序方式存储，它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    pre_node = ListNode(0)
    cur = pre_node
    n = 0
    while l1 or l2:
        n1 = n2 = 0
        if l1:
            n1 = l1.val
            l1 = l1.next
        if l2:
            n2 = l2.val
            l2 = l2.next
        sumnum = n1 + n2 + n
        n = sumnum / 10
        cur.next = ListNode(sumnum % 10)
        cur = cur.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if n > 0:
        cur.next = ListNode(n)
    return pre_node.next


res = addTwoNumbers(l1, l2)
print(res)
