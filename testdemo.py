# coding: utf-8
""" 
@author: oldman
@file: testdemo.py 
@time: 2022-05-17 14:28
"""
import time

def print_time(func):
    def _wrapper(*args, **kwargs):
        print("输入参数是：{}, {}".format(args, kwargs))
        start_time = time.time()

        res= func(args, kwargs)
        end_time= time.time()
        print("执行时间为：{}".format(end_time-start_time))
        print("输出结果是：{}, {}".format(res))
        return res
    return _wrapper

@print_time
def string_to_num(str):
    """
    十一万一 -> 111000
    :param string:
    :return:
    """
    string_map = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10,
                  "万": 10000, "千": 1000, "百": 100, "十": 10, "零":0
                  }

    int_set = {"万", "千", "百", "十"}

    last_dict = {"万":1000, "千":100, "百":10}

    res = 0
    char_num = 1
    char_str = ""
    last_num = ""
    for index in range(len(str)):

        if last_num in last_dict:
            res += string_map[str[index]]*last_dict[last_num]
        else:

            if str[index] not in int_set:
                res += string_map[str[index]]*char_num
            else:
                res += char_num*string_map[str[index]]
        if str[index] in last_dict:
            last_num = str[index]
    return res






string_to_num("十一万一")