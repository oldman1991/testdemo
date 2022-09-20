# coding=utf-8
# create by oldman at 2018/8/26
"""
实现序列协议
"""
import re
import reprlib
from collections import Iterable

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self):
        return len(self.words)

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     return self.words.pop()

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    """
    reprlib.repr这个使用函数用于生成大型数据结构的简略字符串表示形式
    """
Iterable

def test():
    s = Sentence(' "The time has come, " the Walrus said') # 传入一个字符串，创建一个Sentence实例
    print(s) # 注意，__repr__方法的输出中包含reprlib.repr方法生成的...。
    for word in s:  # Sentence 实例可以迭代，稍后说明原因。
        print(word)
    print(list(s))  # 因为可以迭代，所以Sentence 对象可以用于构建列表和其他的可迭代的类型

if __name__ == "__main__":
    test()

"""
序列可迭代的原因:iter函数
解释器需要迭代对象x时，会自动调用iter(x)。
内置的iter函数有以下作用：
(1)检查对象是否实现了__iter__方法，如果实现了就调用它，获取一个迭代器
(2)如果没有事项__iter__方法，但是实现了__getitem__方法，python会创建一个迭代器
尝试按顺序(从索引0开始)获取元素。
(3)如果尝试失败，Python抛出TypeError异常，通常会提示"C object is not iterable"(
C对象不可迭代)，其中C是目标对象所属的类。
任何Python 序列都可迭代的原因是，它们都实现了__getitem__方法。其中标准的序列也都实现了
__iter__方法，因此你也应该这么做。之所以对__getitem__方法做特殊的处理，是为了向后兼容，而未来可能不会再这么做
"""