#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/9/30
"""
with 语句管理上下文
"""


class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True


with LookingGlass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)

print(what)

print('Back to normal!')
