# coding=utf-8
# create by oldman at 2018/6/22
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence(object):
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator(object):
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    @property
    def __iter__(self):
        return self

"""
﻿迭代器：
    迭代器是这样的对象：实现了无参数的__next__方法，
    返回序列中的下一个元素;如果没有元素了，那么抛出StopIteration异常。
    python中的迭代器还实现了__iter__方法，因此迭代器也可以迭代。

可迭代对象有个__iter__方法，每次都实例化一个新的迭代器；
而迭代器要实现__next__方法，返回单个元素，此外还要实现__iter__方法，
返回迭代器本身。
因此，迭代器可以迭代，但是可迭代对象不是迭代器。
可迭代的对象一定不能是自身的迭代器。
也就是说，可迭代的对象必须实现__iter__方法，但不能实现__next__方法
"""


class SentenceNew(object):
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return
        # return iter(self.words)
