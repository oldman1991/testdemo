#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/8/21


"""

田忌赛马
q1<t1<q2<t2<q3<t3
其中q1,q2,q3为齐王的马
t1,t2,t3为田忌的马
"""
q_time = {'q1': 1.0, 'q2': 2.0, 'q3': 3.0}

t_time = {'t1': 1.5, 't2': 2.5, 't3': 3.5}

def compare(t, q):
    t_won_cnt = 0
    for i in range(len(t)):
        print("{} {}".format(t[i], q[i]))
        if t_time[t[i]] < q_time[q[i]]:
            t_won_cnt +=1

    if t_won_cnt > len(t)/2:
        print(u"田忌获胜！")
    else:
        print(u"齐王获胜！")



def  permutate(horses, result):
    """
    使用函数的递归调用和，找出所有可能的马出战顺序
    :param horses: 目前还有多少马没有出战
    :param result: 保存当前已经出战的马以及顺序
    :return:
    """
    q_horses = ["q1", "q2", "q3"]
    if len(horses) == 0:
        print(result)
        compare(result, q_horses)
        return
    for i in range(len(horses)):
        # 从剩下的未出战马匹中，选择一匹，加入结果
        new_result = result.copy()
        new_result.append(horses[i])
        # 将已选择的马匹从未出战的列表中移除
        rest_horses = horses.copy()
        rest_horses.remove(horses[i])
        permutate(rest_horses, new_result)



def arrangement():
    horses = ["t1", "t2", "t3"]
    permutate(horses, [])


arrangement()