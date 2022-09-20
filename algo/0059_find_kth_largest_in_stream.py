#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/3/21
"""

"""
import heapq


class KthLargest(object):
    """
    数据流中的第K大元素，使用优先队列实现
    """

    def __init__(self, k, nums):
        """
        :param k: int
        :param nums: List[int]
        """
        self.pool = nums
        self.size = len(self.pool)
        self.k = k
        # heapq.heapify()将列表原地转换为堆并排序
        heapq.heapify(self.pool)
        while self.size > k:
            heapq.heappop(self.pool)
            self.size -= 1

    def add(self, val):
        """
        :param val: int
        :return: int
        """
        if self.size < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


k = 3
arr = [4, 5, 8, 2]
kth = KthLargest(k, arr)
print(kth.add(5))
print(kth.add(10))
print(kth.add(7))
