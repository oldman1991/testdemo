#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/9/2

"""
函数缓存允许我们将一个函数对于给定参数的返回值缓存起来。
当一个I/O密集的函数被频繁使用相同的参数调用的时候，函数缓存可以节约时间。
"""
import json
from functools import wraps


def memorize(fn):
    memo = {}
    @wraps(fn)
    def wrapper(*args):
        if args in memo:
            print("THIS IS MEMORY")
            return memo[args]
        else:
            rv = fn(*args)
            print("THIS IS value")
            memo[args] = rv
            return rv
    return wrapper


class Memorize:
    def __init__(self, fn):
        self.fn=fn
        self.memo = {}

    def __call__(self, *args):
        s = json.dumps(args)
        if s not in self.memo:
            print("THIS IS value")
            self.memo[s] = self.fn(*args)
        print(111)
        return self.memo[s]



@memorize
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


@Memorize
def fibonacci2(n):
    if n<2:
        return n
    return fibonacci2(n-1) + fibonacci2(n-2)


# print(fibonacci(5))

print(fibonacci2(5))