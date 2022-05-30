# coding: utf-8
""" 
@author: oldman
@file: test_demo01.py 
@time: 2022-05-17 16:03
"""

import datetime


def string_to_dict(info_str):
    """
    字符串转字典
    """
    data_info_list = info_str.split(",")
    _source_type = "lounge"
    source_type = data_info_list[3].split(":")[1]
    if source_type != _source_type:
        return None

    try:
        return {
            "time": datetime.datetime.strptime(data_info_list[0].strip(), "%Y-%m-%d %H:%M:%S"),
        "target_uid":data_info_list[3].split(":")[1],
        "source_type":source_type,
        "gift_id": int(data_info_list[3].split(":")[6]),
        "count": int(data_info_list[3].split(":")[7]),

        }
    except Exception as e:

        return None


def red_log(log_path):
    log_res = []
    with open(log_path, "r") as f:
        while True:
            line = f.readline()
            if line is not None:
                info = string_to_dict(line)
                if info:
                    log_res.append(info)
            else:
                break

    return log_res


"""
2021-03-31 20:00:03,973 INFO  enter send_gift_process function, uid: u1205463919213203456, target_uid: u1614003061086879339, source_type: lounge, 

"""

info = [{
            "time": datetime.datetime.strptime("2021-03-31 20:00:03", "%Y-%m-%d %H:%M:%S"),
        "target_uid":"u1614003061086879339",
        "source_type":"lounge",
        "gift_id": 1000,
        "count": 1,

        },
{
            "time": datetime.datetime.strptime("2021-03-31 20:00:02", "%Y-%m-%d %H:%M:%S"),
        "target_uid":"u1614003061086879339",
        "source_type":"lounge",
        "gift_id": 1000,
        "count": 2,

        },
{
            "time": datetime.datetime.strptime("2021-03-31 20:01:03", "%Y-%m-%d %H:%M:%S"),
        "target_uid":"u1614003061086879339",
        "source_type":"lounge",
        "gift_id": 1000,
        "count": 3,

        },
{
            "time": datetime.datetime.strptime("2021-03-31 20:04:03", "%Y-%m-%d %H:%M:%S"),
        "target_uid":"u1614003061086879339",
        "source_type":"lounge",
        "gift_id": 5001,
        "count": 2,

        }

    ]


def user_gift(info):
    # res = red_log(log_path)
    user_dict = {}
    for item in info:
        target_uid = item["target_uid"]
        if target_uid not in user_dict:
            user_dict[target_uid] = []
        user_dict[target_uid].append(item)
    return user_dict


gift_info = {  # gift_id 和 得分的对应关系
    1000: 1,
    4000: 2,
    5001: 10,
    5002: 90,
    5003: 9990,
    5004: 990,
    5101: 300,
    5102: 3000,
    5103: 70,
    5104: 5550
}


def get_result(info):
    # user_dict = user_gift(log_path)
    # user_dict = info
    user_dict = user_gift(info)
    res = []
    for key, value in user_dict.items():
        count = 0
        min_time, max_time = value[0]['time'], value[0]['time']
        for item in value:
            min_time = min(min_time, item['time'])
            max_time = max(max_time, item['time'])
            count += gift_info[item["gift_id"]] * item["count"]
        res.append({"target_uid": key, "_min_time": min_time,
                    "_max_time": max_time, "count": count})

    for info in res:
        print(
            f'校验收礼人为：”{info["target_uid"]} ” 当天 {info["_min_time"].strftime("%H:%M:%S")}到{info["_max_time"].strftime("%H:%M:%S")} 在歌房(lounge)的得分情况({info["count"]})')


get_result(info)




