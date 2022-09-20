# coding=utf-8
# create by oldman at 2017/10/25
import weakref


class Spam:
    def __init__(self, name):
        self.name = name


_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s


"""
上面的解决方案需要依赖全局变量以及一个与原始的类定义相分离的工厂函数。
一种改进方式是将缓存代码放到另一个单独的管理类中，然后将这些组件粘合在一起
"""


class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam()
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s


class Spam:
    manager = CachedSpamManager()

    def __init__(self, name):
        self.name = name


def get_spam(name):
    return Spam.manager.get_spam(name)


"""
这种方法的特点就是为潜在的灵活性提供了更多的支持。
例如，我们可以实现不同类型的缓存管理机制(以单独的类来实现)， 然后附加到Spaml类中替换掉默认的缓存实现
其他的代码(比如get_spam)不需要修改就能工作。
另外一种设计上的考虑是到底要不要将类的定义暴露给用户。如果什么都不做的话，用户很容易创建出实例，
从而绕过缓存机制；
>>> a = Spam('foo')
>>> b = Spam('foo')
>>> a is b
False
>>>
可以在类名前面加一个下划线，例如_Spam，这样至少可以提醒用户不应该直接去访问他
或者，如果想为用户提供更强的提示，暗示他们不应该直接实例化Spam对象，可以让__Init__()方法抛出一个
异常，然后用一个类方法来实现构造函数的功能，就像下面：
"""


class Spam:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Cant't instanciate directly")

    manager = CachedSpamManager()

    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self


class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam._new(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s


def get_spam(name):
    return Spam.manager.get_spam(name)
