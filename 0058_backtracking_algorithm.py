#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/2/12

"""
回溯算法
八皇后问题
"""


def check(board, pos):
    pass


def eightQueen(board, row):
    blen = len(board)
    if row == blen:  # 来到不存在的第九行了
        print(board)
        return True  # 一定要return一个true
    for possibleY in range(blen):
        if check(board, (row, possibleY)):
            board[row][possibleY] = 1
            if not eightQueen(board, row + 1):
                board[row][possibleY] = 0
            else:
                return True
    return False


"""
0-1
我们有一个背包，背包总的承载重量是 Wkg。现在我们有 n 个物品，每个物品的重量不等，并且不可分割。我们现在期望选择几件物品，装载到背包中。在不超过背包所能装载重量的前提下，如何让背包中物品的总重量最大？
"""

maxW = 0
weight = [2, 2, 4, 6, 3]  # 每个物品的重量
n = 5  # 物品个数
w = 20  # 背包承受的最大重量
res_dict = {}


def f(i, cw):
    """
    :param i: 表示考察到哪个物品了
    :param cw: 表示当前装进去的物品的重量和
    :return:
    """
    """
    递归所有可能出现的情况，看哪一个的结果是优的，一个物品的选择就两种方法，要么放进背包要么不放进背包。
    """
    if cw == w or i == n:  # cw=w,装满了，i=n,表示已经考察完了所有的物品
        global maxW
        if cw > maxW:
            maxW = cw
        return
    if '{}_{}'.format(i, cw) in res_dict:
        return
    res_dict['{}_{}'.format(i, cw)] = True
    f(i + 1, cw)  # 选择不装第i个物品
    if cw + weight[i] <= w:
        f(i + 1, cw + weight[i])  # 选择装第i个物品


f(0, 0)
print(maxW)

"""
背包问题升级
0-1
我们有一个背包，背包总的承载重量是 Wkg。现在我们有 n 个物品，每个物品的重量不等，价值不等，并且不可分割。我们现在期望选择几件物品，装载到背包中。在不超过背包所能装载重量的前提下，如何让背包中物品的总价值最大？
"""
maxW = 0
weight = [2, 2, 4, 6, 3]  # 每个物品的重量
value = [3, 4, 8, 9, 6]
n = 5  # 物品个数
w = 20  # 背包承受的最大重量
res_dict = {}


def f_2(i, cw, cv):
    """
    :param cv: 目前的总价值
    :param i: 第几个物品
    :param cw: 背包目前装的总数量
    :return:
    """
    if cw == w or i == n:  # 装满了或者所有物品都考察完了
        global maxW
        if cv > maxW:
            maxW = cv
        return
    f_2(i + 1, cw, cv)  # 选择不装第i个物品
    if cw + weight[i] <= w:
        f_2(i + 1, cw + weight[i], cv + value[i])  # 选择装第i个物品


f_2(0, 0, 0)
print(maxW)
