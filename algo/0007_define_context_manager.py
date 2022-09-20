# coding=utf-8
# create by oldman at 2017/11/11
"""
问题：
    你想自己去实现一个新的上下文管理器，以便使用with语句

解决方案：
    事项一个新的上下文管理器的最简单的方法就是使用contexlib模块中的
    @contextmanager装饰器，下面是一个实现了代码块及时功能的上下文
    管理器例子：
"""
from contextlib import contextmanager

import time


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end-start))
