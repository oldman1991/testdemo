#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/12/25
"""
>>> t = "this is a big apple,this is a big apple,this is a big apple,this is a big apple."
>>> p = "apple"
>>> bf(t, p)
4
>>> t = "为什么叫向量空间模型呢？其实我们可以把每个词给看成一个维度，而词的频率看成其值（有向），即向量，这样每篇文章的词及其频率就构成了一个i维空间图，两个文档的相似度就是两个空间图的接近度。假设文章只有两维的话，那么空间图就可以画在一个平面直角坐标系当中，读者可以假想两篇只有两个词的文章画图进行理解。"
>>> p = "读者"
>>> bf(t, p)
1
"""
import time

"""
字符串匹配算法
"""


def bf(t, p):
    """
    BF算法 Brute Force 暴力匹配算法，朴素匹配算法
    :param t:主串
    :param p:模式串
    :return:
    """
    start = time.time()
    i = 0
    count = 0
    while i <= len(t) - len(p):
        j = 0
        while t[i] == p[j]:
            if j == len(p) - 1:
                count += 1
                break
            i += 1
            j += 1

        else:
            i += 1
    print(count)
    print(time.time() - start)
    return count


def bf_02(t, p):
    """
    两个 while 循环嵌套，参考Algorithms 4th, Robert Sedgewick, page 760。在内层指针前进时，外层指针不动，直到内从指针循环完以后才前进一位。
    :param t:
    :param p:
    :return:
    """
    start = time.time()
    n = len(t)
    m = len(p)
    res = []
    i = 0
    while i <= (n - m):
        j = 0
        while j < m:
            if t[i + j] != p[j]:
                break
            j += 1
        if j == m:
            res.append(i)
        i += 1
    print(time.time() - start)
    return res


def bf_03(txt, pattern):
    """
    只有一个 while，但也是控制两个指针。如果不匹配，目标文本字符串的指针向前走一位，而模式字符串的指针会到下标 0 的位置。这种方法相当于上一种方法的改进型，特点是两个指针一起前进。、、
    :param txt:
    :param pattern:
    :return:
    """
    N = len(txt)
    M = len(pattern)

    i = 0  # pointer into text
    j = 0  # pointer into pattern

    while i < N and j < M:
        if txt[i] == pattern[j]:
            i += 1
            j += 1
            if j == M:
                return i - j
        else:
            i = i - j + 1
            j = 0
    return -1


t = "this is a big apple,this is a big apple,this is a big apple,this is a big apple."
p = "apple"
bf(t, p)
print(bf_02(t, p))

