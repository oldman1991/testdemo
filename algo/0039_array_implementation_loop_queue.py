#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/10/12

"""
使用python的数组实现固定数量的队列的功能
>>> a = ArrayLoopQueue(3)
>>> a.enqueue(1)
True
>>> a.enqueue(2)
True
>>> a.enqueue(3)
False
>>> a.enqueue(4)
False
>>> a.dequeue()
1
>>> a.enqueue(3)
True
"""


class ArrayLoopQueue(object):
    """
    数组实现循环队列
    """

    def __init__(self, capacity):
        self.head = 0
        self.tail = 0
        self.n = capacity
        self.items = [None] * capacity

    def enqueue(self, item):
        if (self.tail + 1) % self.n == self.head:  # 队列满了
            return False
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.n
        return True

    def dequeue(self):
        if self.tail == self.head:
            return None
        res = self.items[self.head]
        self.head = (self.head + 1) % self.n
        return res
a = ArrayLoopQueue(3)
assert a.enqueue(1)
assert a.enqueue(2)
assert not a.enqueue(3)
assert not a.enqueue(4)
assert a.dequeue() == 1
assert a.enqueue(4)