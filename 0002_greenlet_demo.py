# coding=utf-8
# create by oldman at 2017/10/19
from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)


def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()


def test3(x, y):
    z = gr4.switch(x + y)
    print(z)


def test4(u):
    print(u)
    gr3.switch(42)


gr3 = greenlet(test3)
gr4 = greenlet(test4)
gr3.switch('hello', 'world')
