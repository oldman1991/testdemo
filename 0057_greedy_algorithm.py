#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/1/15

"""
贪心算法
"""


def   greedy_money(m):
    """
    找零问题：假设只有 1 元、 2 元、5元、 10元，20元，50元的纸币。在超市结账 时，如果 需要找零钱， 收银员希望将最少的纸币数找给顾客。那么，给定 需要找的零钱数目，如何求得最少的纸币数呢？
    :param m:要找零的钱数
    :return:
    """
    d = [1, 2, 5, 10, 20, 50]
    d_num = [10, 10, 10, 10, 10, 10]
    s = 0
    for i in range(len(d)):
        s += d[i] * d_num[i]
    print("一共有钱：{}元".format(s))

    if m > s:
        print("找零太多，钱不够")
        return None
    i = len(d) - 1
    while i >= 0:
        if m >= d[i]:
            n = m // d[i]
            if n >= d_num[i]:
                n = d_num[i]
            m -= n * d[i]
            print("使用了{}个{}元纸币".format(n, d[i]))
        i -= 1


greedy_money(12)
greedy_money(12)


def max_sum(list_n):
    """
    最大子数组问题：一个整数数组中的元素有正有负，在该数组中找出一个连续子数组，要求该连续子数组中各元素的和最大，并返回该最大值.
    计算某串子数组A[i:j]，一旦发现sum(A[i:j])<0，那么后面A[i:j+1]之后就无需再计算了，这一组结果一定不满足最大（已经算出了负数，完全可以把这组负数结果抛弃掉，从下一个下标开始算），因此此时应该直接开始算从A[j+1]开始的子数列：

    :param list_n:给定数组
    :return:
    """
    ans = 0
    sums = 0
    for i in list_n:
        sums += i
        ans = max(ans, sums)
        if sums <= 0:
            sums = 0
    return ans


print(max_sum([1, 2, -9, 4, 5, -8, 1, 3, 9, -9, 7, 2, 1]))


def greedy():
    """
    一辆汽车加满油后可行驶n公里。旅途中有若干个加油站。设计一个有效算法，指出应在哪些加油站停靠加油，使沿途加油次数最少。 对于给定的n(n <= 5000)和k(k <= 1000)个加油站位置，编程计算最少加油次数。
    :return:
    """
