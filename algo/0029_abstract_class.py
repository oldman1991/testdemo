# coding=utf-8
# create by oldman at 2018/6/20
import abc
import random

from collections import Iterator


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加元素"""

    @abc.abstractmethod
    def pick(self):
        """
        随机删除元素，然后将其返回
        如果实力为空，这个方法应该抛出 'LookupError'
        :return:
        """

    def loaded(self):
        """
        如果至少有一个元素，则返回true， 否则返回false
        :return:
        """
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序元组，由当前元素组成"""
        items = []
        while True:
            try:
                items.append(self.pick)
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class BingoCage(Tombola):
    """
    :param
    """

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = items
        self.load(items)

    def pick(self):
        try:
            self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def load(self, iterable):
        self._items.extend(iterable)
        self._randomizer.shuffle(self._items)

    def __call__(self, *args, **kwargs):
        self.pick()


class LotteryBlower(Tombola):
    """
    :param
    """

    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))


@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

# Tombola.register(Tombola)

# Iterator
