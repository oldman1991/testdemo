#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/8/30
import uuid

from redis import ConnectionPool
from redis import StrictRedis
import time

from redis import WatchError

pool = ConnectionPool()
redis_client = StrictRedis(connection_pool=pool)

def get_lock(lock_name, code, acquire_time=6, time_out=10):
    """
    获取一个分布式锁
    :param code:
    :param lock_name: 锁的名字
    :param acquire_time: 等待获取锁的时间
    :param time_out:  锁的redis过期时间
    :return:
    """

    end = time.time() + acquire_time
    lock = "distribute:lock:" + lock_name
    while time.time() < end:
        # setnx 如果存在key，则返回False，如果不存在，则setkey，并且返回True，原子操作
        if redis_client.setnx(lock,code):
            # 给锁设置超时时间，防止进程崩溃导致其他进程无法获取锁
            redis_client.expire(lock, time_out)
            return identifier
        # 若果没有设置成功，并且key也没有过期时间
        elif redis_client.ttl(lock)==-1:
            # 设置过期时间
            redis_client.expire(lock, time_out)
        time.sleep(0.001) # 单位是秒
    return False


def release_lock(lock_name, code):
    """
    释放锁函数
    :param lock_name:锁的名字
    :param code:验证码
    :return:
    """
    lock = "distribute:lock" + lock_name
    with redis_client.pipeline(True) as pip:
        while True:
            try:
                # watch库主键，mutli后如果该key被其他客户端改变，事务操作会抛出WatchError异常
                pip.watch(lock)
                lock_value = redis_client.get(lock)
                if not lock_value:
                    return True
                if lock_value.decode() == code:
                    # 事务开始
                    pip.multi()
                    pip.delete(lock)
                    # execute执行结果列表
                    pip.execute()
                    return True
                break
            except WatchError as e:
                pip.unwatch()
                print(e)

    return False

identifier = str(uuid.uuid4())
lock_name = "11"
ideen = "111"
# print(acquire_lock(lock_name,ideen))
print(release_lock(lock_name, ideen))