#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/10/12

"""
使用python的数组实现固定数量的队列的功能
>>> a = ArrayQueue(3)
>>> a.enqueue(1)
True
>>> a.enqueue(2)
True
>>> a.enqueue(3)
True
>>> a.enqueue(4)
False
>>> a.dequeue()
1
>>> a.enqueue(3)
True
"""


class ArrayQueue():
    def __init__(self, capacity):
        self.head = 0
        self.tail = 0
        self.items = [None] * capacity
        self.n = capacity

    def enqueue(self, item):
        """
        入栈
        :return:
        """
        if self.tail == self.n:  # 数组末尾已被占用
            if self.head == 0:  # 表示队列已被占满
                return False
            for i in range(self.head, self.tail):  # 队列没有满，整体移动数组向前
                self.items[i - self.head] = self.items[i]
            self.tail -= self.head
            self.head = 0
        self.items[self.tail] = item
        self.tail += 1
        return True

    def dequeue(self):
        """
        出栈
        :return:
        """
        if self.head == self.tail:
            return None
        else:
            res = self.items[self.head]
            self.head += 1
            return res


a = ArrayQueue(3)
assert a.enqueue(1)
assert a.enqueue(2)
assert a.enqueue(3)
assert not a.enqueue(4)
assert a.dequeue() == 1
