#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/12/18


class Heap(object):
    """
    堆
    """

    def __init__(self, n):
        self.a = []  # 列表，从下标1开始存储数据
        self.n = n  # 堆可以存储的最大数据个数
        self.count = 0  # 堆中已经存储的数据格式

    def insert(self, data):
        """
        向堆中插入一条数据
        :param data:
        :return:
        """
        if self.count >= self.n:
            return
        self.count += 1
        i = self.count
        self.a[self.count] = data
        while i // 2 > 0 and self.a[i] > self.a[i // 2]:
            self.a[i], self.a[i // 2] = self.a[i // 2], self.a[i]
            i //= 2

    def remove_max(self):
        if self.count == 0:
            return None
        self.a[1] = self.a[self.count]
        self.count -= 1
        self.heapify(self.a, self.count, 1)

    def heapify(self, a, n, i):
        """
        自上而下堆化
        :param a:
        :param n:
        :param i:
        :return:
        """
        while True:
            maxPos = i
            if i * 2 <= n and a[i] < a[i * 2]:
                maxPos = i * 2
            if i * 2 + 1 <= n and a[maxPos] < a[i * 2]:
                maxPos = i * 2 + 1
            if maxPos == i:
                break
            a[i], a[maxPos] = a[maxPos], a[i]
            i = maxPos
