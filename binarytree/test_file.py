# coding: utf-8
""" 
@author: oldman
@file: test_file.py 
@time: 2022/8/19 09:20
"""
import datetime
import operator
import re


def read_file():
    p1 = re.compile(r'[(](.*?)[)]', re.S)
    str_list = []
    with open("1.csv", "r") as f:
        line = f.readline()
        while line:
            _time = line.split("|")[0].replace("'", "").replace('"', "").replace("[", "")
            _str_list = re.findall(p1, line)
            if len(_str_list) > 0:
                str_list.append(_time + "," + _str_list[0])
            line = f.readline()
    return str_list


if __name__ == "__main__":
    res = []
    count = 0
    str_list = read_file()
    for item in str_list:
        _strs = item.replace("\\", "").split(",")
        _time = datetime.datetime.strptime(_strs[0], '%Y-%m-%d %H:%M:%S')
        user_id = _strs[6].split(":")[1].replace("'", "")
        product_id = _strs[9].split(":")[1].replace('"', "")
        order_id = _strs[8].split(":")[2].replace('"', "")
        token = _strs[10].split(":")[1].replace('"', "")
        # if user_id in res:
        #     _item = res[user_id]
        #     if product_id==_item["product_id"] and order_id == _item["order_id"] and token == _item["token"]:
        #         continue
        #     else:
        #         count+=1
        # else:
        res.append({
            "user_id": user_id,
            "product_id": product_id,
            "order_id": order_id,
            "token": token,
            "_time": _time
        })

    res.sort(key=operator.itemgetter("_time"))
    print(res)
