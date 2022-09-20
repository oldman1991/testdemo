# coding: utf-8
""" 
@author: lipeng
@file: 0098_meta_programming.py 
@time: 2020/01/05
"""


class MyMeta(type):
    def __new__(mcs, name, bases, cls_dict):
        """
        元类创建类对象的方法
        :param name: 类对象的名字
        :param bases: 类对象的父类
        :param cls_dict: 类对象的命名空间
        :return:
        """
        print(f"call MyMeta __new__ method, mcs:{mcs}")
        return super().__new__(mcs, name, bases, cls_dict)

    def __init__(cls, name, bases, cls_dict):
        """
        类对象创建完后的初始化
        :param name:
        :param bases:
        :param cls_dict:
        """
        print(f"call MyMeta __init__ method, cls:{cls}")
        super().__init__(name, bases, cls_dict)

    @classmethod
    def __prepare__(mcs, name, bases):
        """
        类对象和创建完之前的准备工作，返回一个字典
        用于为类对象创建命名空间
        :param name:
        :param bases:
        :return:
        """
        print(f"call MyMeta __prepare__ method, mcs:{mcs}")
        return super().__prepare__(name, bases)

    def __call__(cls, *args, **kwargs):
        """
        用于为类对象创建实例对象时调用
        :param args:
        :param kwargs:
        :return:
        """
        print(f"call MyMeta __call__ method, cls:{cls}")
        return super().__call__(*args, **kwargs)


class MyClass(metaclass=MyMeta):
    def __new__(cls, *args, **kwargs):
        print(f"call MyClass __new__ method, cls:{cls}")
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print(f"call MyClass __init__ method, self:{self}")


a = MyClass()

