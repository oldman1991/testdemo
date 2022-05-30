# coding=utf-8
# create by oldman at 2017/10/20
import imp
import operator
from itertools import accumulate

from functools import reduce

imp.find_module('itertools')
data = [3, 4, 6, 2, 1, 9, 7, 5, 8]
result = accumulate(data)
print(list(accumulate(data, operator.mul)))
print(list(accumulate(data)))


def add(x):
    return x * x


res = map(add, data)
print(list(res))

res1 = reduce(lambda x, y: x * y, data)
print(res1)
