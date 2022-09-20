# coding: utf-8
""" 
@author: oldman
@file: test_google_verify.py 
@time: 2022/8/19 17:32
"""
import re


def handler_log():
    p1 = re.compile(r'[<](.*?)[>]', re.S)
    str_list = []
    with open("2.csv", "r") as f:
        line = f.readline()
        while line:
            _time = line.split("|")[0].replace("'", "").replace('"', "").replace("[", "")
            _str_list = re.findall(p1, line)
            if len(_str_list) > 0:
                str_list.append(_str_list[0])
            line = f.readline()
    return str_list



if __name__ == "__main__":
    res = handler_log()
    for i in res:
        print(i)