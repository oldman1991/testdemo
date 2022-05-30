# coding=utf-8
import sys


def test_break():
    for i in range(0,9):
        if i==3:
            break
        print(i)

if __name__=="__main__":
    test_break()