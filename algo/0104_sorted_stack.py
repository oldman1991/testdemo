# coding: utf-8
""" 
@author: oldman
@file: 0104_sorted_stack.py 
@time: 2022-05-30 11:57
"""
"""
栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，
但不得将元素复制到别的数据结构（如数组）中。该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，pee


"""

class SortedStack:

    def __init__(self):
        self.stack = []
        self.tmp = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
        else:
            while self.stack and self.stack[-1] < val:
                self.tmp.append(self.stack.pop())
            self.stack.append(val)
            while self.tmp:
                self.stack.append(self.tmp.pop())


    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()
        return None


    def peek(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def isEmpty(self) -> bool:
        return not self.stack

