#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/6/17


"""
属性查找
"""


class Animal:
    run = True


class Dog(Animal):
    fly = False

    def __init__(self, age):
        self.age = age

    def sound(self):
        return "wangwang"

    # 重写__getattribute__。需要注意的是重写的方法中不能
    # 使用对象的点运算符访问属性，否则使用点运算符访问属性时，
    # 会再次调用__getattribute__。这样就会陷入无限递归。
    # 可以使用super()方法避免这个问题。
    def __getattribute__(self, key):
        print("calling __getattribute__\n")

        return super(Dog, self).__getattribute__(key)

    def __getattr__(self, name):
        print("calling __getattr__\n")

        if name == 'adult':
            return True if self.age >= 2 else False
        else:
            raise AttributeError

    def __setattr__(self, name, value):
        print("calling __setattr__")

        super(Dog, self).__setattr__(name, value)
    #
    # def __delattr__(self, name):
    #     print("calling __delattr__")
    #
    #     super(Dog, self).__delattr__(name)


# dog = Dog(1)
# print(dog.__dict__)
#
# print(Dog.__dict__)
# print(Animal.__dict__)
#
# print(dog.age)
# print(dog.fly)
# print(dog.run)
# print(dog.sound)



"""
描述符
"""


class RevealAccess(object):
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val


class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5


# m = MyClass()
# print(m.__dict__)
# print(MyClass.__dict__)
# # print(m.x)
# print(m.x)
# m.x = 30
# print(m.x)
# print(m.__dict__)


# 使用描述符做延迟加载


class lazy(object):
    def __init__(self, func):
        self.func = func  # lazy的实例属性func等于area方法对象

    def __get__(self, instance, cls):
        val = self.func(instance)  # 调用area方法计算出结果
        setattr(instance, self.func.__name__, val)  # 将结果设置给c的area属性
        return val


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @lazy  # area = lazy(area) lazy描述符
    def area(self):
        print('evalute')
        return 3.14 * self.radius ** 2


c = Circle(4)
print(c.radius)
print(c.__dict__)
print(c.area)
print(c.__dict__)
print(c.area)
print(c.area)
