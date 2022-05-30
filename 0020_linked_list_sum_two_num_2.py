# coding=utf-8
# create by oldman at 2018/4/5
"""

给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。



你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶:

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

解题思路：使用栈结构
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Stack:
    """模拟栈"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = Stack()
        s2 = Stack()
        n = 0
        cur_node = ListNode(-1)
        while l1:
            s1.push(l1.val)
            l1 = l1.next
        while l2:
            s2.push(l2.val)
            l2 = l2.next
        while (not s1.isEmpty()) or (not s2.isEmpty()) or n:
            num1 = s1.pop() if not s1.isEmpty() else 0
            num2 = s2.pop() if not s2.isEmpty() else 0
            sumnum = num1 + num2 + n
            n = sumnum / 10
            cur_node.val = sumnum % 10
            pre_node = ListNode(-1)
            pre_node.next = cur_node
            cur_node = pre_node

        return cur_node.next
