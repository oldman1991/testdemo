# coding: utf-8
""" 
@author: lipeng
@file: 0099_singleton_with_metaclass.py 
@time: 2020/01/05
"""


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls._instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class SingletonCls(metaclass=Singleton):
    def __init__(self):
        print('call SingletonCls init method')


if __name__ == '__main__':
    s1 = SingletonCls()
    s2 = SingletonCls()
    print(s1 is s2)
