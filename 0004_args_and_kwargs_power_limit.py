# coding=utf-8
# create by oldman at 2017/11/7
"""
对于任何涉及到操作函数调用签名的问题，你都应该使用inspect 模块中的签名特性。
我们最主要关注两个类：Signature 和 Parameter.
下面是一个创建函数前面的交互例子：
>>> from inspect import Signature, Parameter
>>> # Make a signature for a func(x, y=42, * z=None)
>>> parms = [ Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
...          Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
...          Parameter('z', Parameter.KEYWORD_ONLY,default=None)
...                                            ]
>>> sig = Signature(parameters=parms)
>>> print(sig)
(x, y=42, *, z=None)

一旦你有了一个签名对象，你就可以使用它的bind()方法很容易的将它绑定到*args和**kwargs上去，
下面是一个简单的演示：
>>> def func(*args, **kwargs):
...     bound_valus = sig.bind(*args, **kwargs)
...     for name, value in bound_valus.arguments.items():
...            print(name, value)
>>> # Try various example
>>> func(1,2,z=3)
x 1
y 2
z 3
>>> func(1)
x 1
>>> func(1,z=3)
x 1
z 3
>>> func(y=2, x=1)
x 1
y 2

可以看出来，通过将签名和传递的参数绑定起来，可以强制函数调用遵循特定的规则，
比如必填，默认，重复等等
下面是一个强制函数签名更具体的例子，在代码中我们在基类中先定义了一个非常通用的
__init__()方法，然后我们强制所有的子类必须提供一个特定的参数签名
"""
import inspect
from inspect import Parameter


def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return inspect.Signature(parms)


class Structure:
    __signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


# Example use
class Stock(Structure):
    """
    # >>> import inspect
    # >>> print(inspect.signature(Stock))
    # (name, share, price)
    # >>> s1= Stock('ACME', 100, 490.1)
    # >>> s2 = Stock('ACME', 100)
    # Traceback (most recent call last):
    # ...
    # TypeError: 'price' parameter lacking default value
    # >>> s3 = Stock('ACME', 100, 490.1, share=50)
    # Traceback (most recent call last):
    # ...
    # TypeError: multiple values for argument 'shares'
    """
    __signature__ = make_sig('name', 'share', 'price')


class Point(Structure):
    """

    """
    __signature__ = make_sig('x', 'y')


"""
讨论：
在我们需要构建通用函数库，编写装饰器或者实现代理的时候，对于 *args和**kwargs 的使用是很普遍的。
但是，这样的函数有一个缺点就是当你想要实现自己的参数检验时，代码就会笨拙混乱，
在最后的一个案例实例中，我们还可以通过使用自定义元类来创建签名对象。下面展示怎样来实现：

"""


class StructureMeta(type):
    def __new__(cls, clsname, base, clsdict):
        clsdict['__signature__'] = make_sig(*clsdict.get('_fields', []))
        return super().__new__(cls, clsname, base, clsdict)


class StructureOne(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


# Example
class StockOne(StructureOne):
    _fields = ['name', 'shares', 'price']


class PointOne(StructureOne):
    _fields = ['x', 'y']


print(inspect.signature(StockOne))

stockone = StockOne(1, 2, 3)
