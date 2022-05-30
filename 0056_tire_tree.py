#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/1/14


class TireNode(object):
    """
    字典树
    代码实现了最简单的字典树，只支持由小写字母组成的字符串。
在此代码基础上扩展一下，就可以实现比较复杂的字典树，比如带统计数的，或支持更多字符的字典树，
或者是支持删除等操作
    Tire树的优势并不在用它来做动态集合数据的查找，因为，这个工作完全可以用更加合适的散列表或者红黑树来替代。Tire树最有优势的是查找前缀匹配的字符串，比如搜索引擎中的关键词提示功能这个场景，就比较适合用它来解决，也是Tire树比较经典的应用场景
    """

    def __init__(self):
        # 是否构成一个完成的单词
        self.is_word = False
        self.children = [None] * 26


class Tire(object):
    def __init__(self):
        self.root = TireNode()

    def add(self, s):
        p = self.root
        n = len(s)
        for i in range(n):
            if p.children[ord(s[i]) - ord('a')] is None:
                new_node = TireNode()
                p.children[ord(s[i]) - ord('a')] = new_node
                p = new_node
            else:
                p = p.children[ord(s[i]) - ord('a')]
            if i == n - 1:
                p.is_word = True

    def search(self, s):
        p = self.root
        for c in s:
            p = p.children[ord(c) - ord('a')]
            if p is None:
                return False
        if p.is_word:
            return True
        else:
            return False

if __name__ == "__main__":
    tire = Tire()
    tire.add('str')
    tire.add('acb')
    tire.add('acblde')
    print(tire.search('acb'))
    print(tire.search('ac'))
    tire.add('ac')
    print(tire.search('ac'))
