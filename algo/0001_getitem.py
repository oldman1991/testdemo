# coding=utf-8
# create by oldman at 2017/10/18


class MyClass(object):
    """
    __getitem__拦截索引运算符：当实例X出现在X【i】这样的索引运算中时，
    Python会调用这个实例继承的__getitem__方法（如果有的话）
    把X作为第一个参数传递，并且方括号内的索引值传给第二个参数
    before python 2.2
    for ... in ... 也是会调用__getitem__() 方法
    要想是想类类对象的可迭代，需要手动实现__getitem__()方法
    """

    def __init__(self):
        self.item = 1211

    def __getitem__(self, index):
        return index * 2


myclass = MyClass()
print(dir(myclass))
print(myclass[2])

for item in myclass:
    print(item)
    break


class MyClass1:
    """
    since python 2.2
    Instead of using the __getitem__ interface, for-in now starts by looking for an __iter__ hook

    If present, this method is called, and the resulting object is then used to fetch items, one by one. This new protocol behaves like this:

obj = train.__iter__()
name = obj.next()
do something with name
name = obj.next()
do something with name
...
where obj is an internal variable, and the next method indicates end of data by raising the StopIterator exception, instead of IndexError
    """
    def __iter__(self):
        return self

    def __next__(self):
        return 1

for item in MyClass1():
    print(item)
    break


