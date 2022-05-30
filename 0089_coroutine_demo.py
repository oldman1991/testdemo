# coding: utf-8
""" 
@author: lipeng
@file: 0089_coroutine_demo.py 
@time: 2019/11/14
"""

# import time
#
#
# def coroutine(func):
#     def ret():
#         f = func()
#         f.__next__()
#         return f
#
#     return ret
#
#
# @coroutine
# def consume():
#     print("Wait to getting a task")
#     while True:
#         n = (yield)
#         print("Got {}".format(n))
#
#
# def producer():
#     c = consume()
#     task_id = 0
#     while True:
#         time.sleep(1)
#         print("Send a task to consumer".format(task_id))
#         c.send(task_id)
#         task_id+=1
#
#
# if __name__ == "__main__":
#     producer()
# import gevent
#
#
# def foo():
#     print("Runing in foo")
#     gevent.sleep(0)
#     print('Explicit context switch to foo again')
#
#
# def bar():
#     print('Explicit context to bar')
#     gevent.sleep(0)
#     print('Implicit context switch to bar')
#
#
# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar)
# ])
# import random
#
# import gevent
#
#
# def task(pid):
#     gevent.sleep(random.randint(0, 2) * 0.001)
#     print('Task {} done'.format(pid))
#
#
# def synchronous():
#     for i in range(5):
#         task(i)
#
#
# def asyncronous():
#     threads = [gevent.spawn(task, i) for i in range(5)]
#     gevent.joinall(threads)
#
#
# print('Synchronous:')
# synchronous()
# print('Asynchronous')
# asyncronous()
# import time
#
# import gevent
#
#
# def handler():
#     while True:
#         print("aaa")
#         time.sleep(1)
#
#
#
# def do():
#     while True:
#         gevent.spawn(handler)
#         gevent.sleep(0.1)
#         print("bbb")
#
#
# do()
import socket

import gevent

urls = ["www.baidu.com", "www.gevent.org", "www.python.org"]
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=5)

print([job.value for job in jobs])
