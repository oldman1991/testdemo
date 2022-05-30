# coding: utf-8
""" 
@author: lipeng
@file: 0096_meta_class_control_create_instance.py 
@time: 2020/01/04
"""
import weakref

"""
使用元类控制实例的创建
"""


class Cashed(type):
    def __init__(cls, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        cls._cache = weakref.WeakValueDictionary()

    def __call__(cls, *args, **kwargs):
        if args in cls._cache:
            return cls._cache[args]
        else:
            obj = super().__call__(*args)
            cls._cache[args] = obj
            return obj


class Spam(metaclass=Cashed):
    def __init__(self, name):
        print("Creating Spam({!r})".format(name))
        self.name = name


a = Spam("Guido")
b = Spam("Diana")
c = Spam("Guido")
print(a is c)
print(type(Spam))
