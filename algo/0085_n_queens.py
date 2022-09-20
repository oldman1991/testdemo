#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/9/3
"""
n皇后问题

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

"""

class Solution:

    def solveNQueens(self, n):
        if n <1:
            return []
        self.result = []
        self.cols = set()
        self.pie = set()
        self.na = set()
        self.DFS(n,0,[])
        return self._generate_result(n)

    def DFS(self, n, row, cur_state):
        if row >=n:
            self.result.append(cur_state)
            return
        for col in range(n):
            if col in self.cols or row+col in self.pie or row-col in self.na:
                # 不满足情况，die
                continue
            # 更新状态
            self.cols.add(col)
            self.pie.add(row+col)
            self.na.add(row-col)

            # DFS遍历
            self.DFS(n, row+1, cur_state+[col])

            # 恢复现场
            self.cols.remove(col)
            self.pie.remove(row+col)
            self.na.remove(row-col)

    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append("."*i + "Q" + "."*(n-i-1))

        return [board[i:i+n] for i in range(0, len(board), n)]

