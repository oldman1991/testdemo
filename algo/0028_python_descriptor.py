# coding=utf-8
# create by oldman at 2018/6/17
"""
python中的描述符
"""

class Des(object):
    def __init__(self, init_value):
        self.value = init_value

    def __get__(self, instance, owner):
        print('call__get', instance, owner)
        return self.value

    def __set__(self, instance, value):
        print('call __set__', instance, value)
        self.value = value

    def __delete__(self, instance):
        print('call __delete__', instance)

        # def __setattr__(self, key, value):
        #     print('call __setattr__',key,value)
        #     self.value=value


class Widget():
    t = Des(1)


def main():
    w = Widget()
    print(type(w.t))
    w.t = 11
    print(222222)
    print(w.t, Widget.t)
    print(333333)
    del w.t


if __name__ == '__main__':
    main()


class lazy(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        val = self.func(instance)
        setattr(instance, self.func.__name__, val)
        return val
        # def __set__(self, instance, value):
        #     pass


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @lazy
    def area(self):
        print('evalute')
        return 3.14 * self.radius ** 2

    def __getattr__(self, item):
        return 1


c = Circle(4)
print(c.radius)
print(c.area)
print(c.area)
print(c.a)
