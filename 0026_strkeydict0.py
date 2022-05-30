# coding=utf-8
# create by oldman at 2018/6/11

import collections


class StrKeyDict0(dict):  # 继承了dict
    """
    查询的时候把非字符串转换为字符串
    """

    def __missing__(self, key):
        if isinstance(key, str):  # 如果找不到的键本身就是字符串，那就抛出KeyError的异常
            raise KeyError(key)
        return self[str(key)]  # 若果找不到的键不是字符串，那么就把它转换成字符串再进行查找

    def get(self, key, default=None):  # get方法把查找工作用self[key]形式委托给__getitem__,这样在
        try:  # 查找失败之前，还能通过__missing__再给某键一个机会
            return self[key]
        except Exception:  # 如果抛出default,那么说明__missing__也失败了，于是返回default
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()  # 先按照传入键的原本的值去查找(我们的映射类型中可能含有非字符串的键
        # )，如果没有找到，再用str()方法把键转换成字符串再查找一次


class StrKeyDict(collections.UserDict): # StrKeyDict 是对UserDict的扩展
    def __missing__(self, key):  # missing方法和上面一模一样
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key): # contains方法更简洁一些，这里可以放心假设所有已经存在的键都是字符串。
        return str(key) in self.keys() # 因此，只要在self.data上查询就好了，并不需要像StrKeyDict0那样去麻烦

    def __setitem__(self, key, value):  # setitem会把所有的键都转换为字符串，由于把具体的实现委托给了self.data属相，这个方法写起来也不难
        self.data[str(key)] = value
    """
两种实现
    """
