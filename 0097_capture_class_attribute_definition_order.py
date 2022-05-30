# coding: utf-8
""" 
@author: lipeng
@file: 0097_capture_class_attribute_definition_order.py 
@time: 2020/01/05
"""
from collections import OrderedDict

"""
问题： 你想自动记录一Ty   个类中属性和方法定义的顺序，然后可以利用它来做很多的操作，
      （比如序列化、映射到数据库等等）

解决方案：利用原来可以很容易的捕捉类的定义信息。
"""
"""
下面是一个例子，使用了一个OrderedDict来记录描述器的定义顺序
"""


class Typed:
    _expected_type = type(None)

    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError('Expected' + str(self._expected_type))
        instance.__dict__[self._name] = value


class Integer(Typed):
    _expected_type = int


class Float(Typed):
    _expected_type = float


class String(Typed):
    _expected_type = str


class OrderMeta(type):

    def __new__(mcs, cls_name, bases, cls_dict):
        d = dict(cls_dict)
        order = []
        for name, value in cls_dict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(mcs, cls_name, bases, d)

    @classmethod
    def __prepare__(mcs, name, bases):
        return OrderedDict()


class Structure(metaclass=OrderMeta):
    def as_csv(self):
        return ','.join(str(getattr(self, name)) for name in self._order)


class Stock(Structure):
    name = String()
    share = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.share = shares
        self.price = price


s = Stock("Good", 100, 490.1)
print(s.name)
print(s.as_csv())
t = Stock("APPL", 'a lot', 610.23)
"""
本节一个关键点就是OrderedMeta元类中定义的 `` __prepare__()`` 方法。 
这个方法会在开始定义类和它的父类的时候被执行。它必须返回一个映射对象以便在类定义体中被使用到。 
我们这里通过返回了一个OrderedDict而不是一个普通的字典，可以很容易的捕获定义的顺序。

如果你想构造自己的类字典对象，可以很容易的扩展这个功能，比如，下面的这个修改方案可以防止重复的定义：
"""


class NoDupOrderedDict(OrderedDict):
    def __init__(self, cls_name):
        self.cls_name = cls_name
        super().__init__()

    def __setitem__(self, key, value):
        if key in self:
            raise TypeError('{} already defined in {}'.format(key, self.cls_name))
        super().__setitem__(key, value)


class OrderedMeta(type):
    def __new__(mcs, cls_name, bases, cls_dict):
        d = dict(cls_dict)
        d['_order'] = [name for name in cls_dict if name[0] != "_"]
        return type.__new__(mcs, bases, d)

    @classmethod
    def __prepare__(mcs, name, bases):
        return NoDupOrderedDict()

"""
下面我们测试重复的定义会出现什么情况：

>>> class A(metaclass=OrderedMeta):
... def spam(self):
... pass
... def spam(self):
... pass
...
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 4, in A
    File "dupmethod2.py", line 25, in __setitem__
        (name, self.clsname))
TypeError: spam already defined in A
>>>
最后还有一点很重要，就是在 __new__() 方法中对于元类中被修改字典的处理。 尽管类使用了另外一个字典来定义，在构造最终的 class 对象的时候， 
我们仍然需要将这个字典转换为一个正确的 dict 实例。 通过语句 d = dict(clsdict) 来完成这个效果。


对于很多应用程序而已，能够捕获类定义的顺序是一个看似不起眼却又非常重要的特性。 例如，在对象关系映射中，我们通常会看到下面这种方式定义的类：

class Stock(Model):
    name = String()
    shares = Integer()
    price = Float()
在框架底层，我们必须捕获定义的顺序来将对象映射到元组或数据库表中的行（就类似于上面例子中的 as_csv() 的功能）。 
这节演示的技术非常简单，并且通常会比其他类似方法（通常都要在描述器类中维护一个隐藏的计数器）要简单的多。

"""
