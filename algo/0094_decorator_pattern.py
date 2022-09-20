# coding: utf-8
""" 
@author: lipeng
@file: 0094_decorator_pattern.py 
@time: 2019/12/27
"""
"""
装饰圈模式是继承方式的一个代替方案。可以轻量级的扩展被装饰对象的功能

"""


class Beverage:
    name = ""
    price = ""
    type = "BEVERAGE"

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


class Coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class Milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0
