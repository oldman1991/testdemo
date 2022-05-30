# coding=utf-8

class A(object):
    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args)
        print(kwargs)
        print("-------------")
        return super(A, cls).__new__(cls)

    def __init__(self, a, b):
        print("init gets calles")
        print(" self is ", self)
        self.a, self.b = a, b


a1 = A(1, 2)
print(a1.a)
print(a1.b)
