#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/9/2
"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""
class Solution:

    def generateParenthesis(self, n):
        self.list = []
        self._gen(0,0,n,"")
        return self.list

    def _gen(self, left, right, n, result):
        """
        :param left: 左括号的个数
        :param right: 右括号的个数
        :param n: n
        :param result: 当前的字符春
        :return:
        """
        if left ==n and right ==n:
            self.list.append(result)
        if left<n:
            self._gen(left+1, right, n, result+')')
        if left>right and right<n:
            self._gen(left, right+1,n, result+"(")