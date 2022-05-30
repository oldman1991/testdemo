# coding=utf-8
# create by oldman at 2018/8/26
"""
第二版Sentence类根据《设计迷失：可复用面向对象软件的基础》一书给出的模型，事项
电影的迭代器设计模式。注意，这不符合Python的习惯做法，后面重构时会说明原因，不过通过这一版能明确
可迭代的集合和迭代器对象之间的关系
"""
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):  # 与前一版本相比，这里只多了一个__iter__方法。这一版没有__getitem__方法，为的是明确表明
        # 这个类可以迭代，因为实现了__iter__方法
        return SentenceIterator(self.words) # 根据可迭代协议，__iter__方法实例化并返回一个迭代器


class SentenceIterator:
    def __init__(self, words):
        self.words = words  # SentenceIterator实例引用单词列表
        self.index = 0  # self.index用于确定下一个要获取的单词

    def __next__(self):
        try:
            word = self.words[self.index] # 获取self.index索引位桑的单词
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self): # 事项self.__iter__方法
        return self
