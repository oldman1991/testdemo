#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/1/11
"""
有四种面额的纸币(1, 2, 5, 10)，使用递归去实现所有的组合为10元的可能性
使用数学归纳法的思想泛化成更一般情况，数学归纳法考虑了两种情况：
    1.初始状态，也就是n=1的时候，命题是否成立；
    2.如果n=k-1的时候，命题成立，那么只要证明n=k的时候，命题也成立。其中k为大于1的自然数
将上述两点顺序更换一下，再抽象一下，是不是这样的地推关系：
    1.假设n=k-1的时候，问题已经解决(或者已经找到解)。那么只要求解 n=k的时候，问题热乎个解决(或者解是多少)；
    2.初始状态，就是n=1的时候，会有多少的解
递归
"""
import copy


class Recursive:
    """
    有多少的解法
    """

    def __init__(self):
        self.rewards = [1, 2, 5, 10]

    def get(self, total_record, result=[]):
        """
        从赏金的总金额开始，每次嵌套调用的时候减去一张纸币的金额，直到所剩的金额为0或者少于0，然后结束爱去哪套调用，开始返回结果值
        :param total_record:
        :param result:
        :return:
        """
        # 当total_record=0时，证明他满足条件的解，结束嵌套调用，输出结果
        if total_record == 0:
            print(result)
        # 当total_record <0 时，证明他不是满足条件的解，不输出
        elif total_record < 0:
            return
        else:
            for i in self.rewards:
                new_result = copy.copy(result)
                new_result.append(i)
                self.get(total_record - i, new_result)


re = Recursive()
re.get(10)


def get_product(product, num, result):
    """
    一个整数可以被分解为多个整数的乘积，例如6可以分解为2*3，请使用递归编程的方法，为给定的整数n，找到所有可能的分级(1在一个解中最多只能出现一次)
    :param num:
    :param result:
    :return:
    """
    pass
