# coding=utf-8
# create by oldman at 2018/8/30
"""
实现相同功能，但却符合Python习惯的方式是，用生成器函数代替
SentenceIterator类。
"""
import re
import reprlib

RE_WORD = re.complie('\w+')


class Sentence(object):
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for world in self.words:
            yield world

        return
