# coding=utf-8
# create by oldman at 2017/11/9
"""
问题：
    我们正在编写一个类，而我们不得不重复定义一些执行了相同任务的属性方法，
    比如说做类型检查。我们想简化代码，解决代码重复的问题。

解决方案：
    考虑下面这个简单的类，这里的属性都用property方法进行了包装：
"""
from functools import partial


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be a string')
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('age must be a int')
        self._age = value


"""
可以看到，为了事项属性值的类型检查我们写了很多的重复代码，只要你以后看到类似的代码，
你都应该想办法去简化他，一个可行的方法是 创建一个函数用来定义属性并返回它。例如：
"""


def typed_property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}'.format(name, expected_type))
        setattr(self, storage_name, value)

    return prop


# Example

class Person:
    name = typed_property('name', str)
    age = typed_property('age', int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


# if __name__ == "__main__":
#     person = Person('name', 13)
#     print(person.age)

"""
讨论：
    本节我们演示内部函数或者闭包的一个重要特性，他们很像一个宏。例子中的函数 typed_property()看上去有点难理解，
    其实它所做的仅仅就是为你生成属性并返回这个属性对象。
    因此，当你在一个类中使用它的时候，效果跟将它里面的代码放在类定义中去是一样的。尽管属性的getter和setter方法
    访问了本地变量如name, expected_type 以及storate_name,这个很正常，这些变量的值会保存在闭包当中。
    我们还可以使用functools.partial()来稍稍改变下这个例子，很有趣。例如，你可以像下面这样：
"""

String = partial(typed_property, expected_type=str)
Integer = partial(typed_property, expected_type=int)


# Example
class Person1:
    name = String('name')
    age = Integer('age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    # p1 = Person1('xiaoming', 'aa')  error
    p1 = Person1('xiaoming', 19)
    print(p1.age)

"""
是不是很优秀^_^……………………
"""