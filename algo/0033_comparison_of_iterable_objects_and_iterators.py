# coding=utf-8
# create by oldman at 2018/8/26
"""
可迭代的对象
    使用iter内置函数可以获取迭代器的对象。如果对象实现了能返回迭代器的__iter__方法，那么对象就是可迭代的。
    序列都可以迭代：实现了 __getitem__方法，而且其参数是从零开始的索引，这种对象也可以迭代。
我们要明确可迭代对象和迭代器之间的关系：Python从可迭代的对象中获取迭代器

标准的迭代器接口有两个方法：
__next__ 返回一个可用的元素，如果没有了元素，抛出StopIteration异常
__iter__ 返回self，以便在应该使用可迭代对象的地方使用迭代器，例如在for循环中
"""
import re
import reprlib

"""
使用生成器函数实现Sentence
"""

RE_WORD = re.complie('\w+')


class Sentence():
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findeall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return

