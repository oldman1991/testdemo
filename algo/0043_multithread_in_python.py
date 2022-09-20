#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/10/18

"""
测试python中多线程的效率低(由于GIL的原因)

True
"""

import threading
import time


def count(n):
    while n > 0:
        n -= 1


t1 = time.time()

count(20000000)
count(20000000)
t2 = time.time()
a = threading.Thread(target=count, args=(20000000,))
a.start()
b = threading.Thread(target=count, args=(20000000,))
b.start()
a.join()
b.join()
t3 = time.time()
assert t2 - t1 < t3 - t2
print(t2 - t1)
print(t3 - t2)
"""

上述的例子是一个很典型的CPU密集任务，threading是Python高级别的线程库，Count只是普通的函数运行在一个主线程内。这就是为什么Python多线程的并不是真正意义上的多线程。Python的Thread是真实操作系统的Thread，两者没有差别。在Linux下是由pthreads实现的，而在windows下是由Windows threads实现的，并通过操作系统调度算法进行调度。为了充分利用CPU，python计算当前已执行了多少数量的指令达到阈值就会立即(100 ticks)来释放GIL。
我们分析一下程序问题：
count函数里面主要做的是计算,I/O操作一直没有触发，那么就会一直等待知道100 ticks才会释放GIL。从释放GIL到获取GIL之间几乎是没有间隙的。所以在其他核心上的线程被唤醒时，大部分情况下主线程已经又再一次获取到GIL了。这个时候被唤醒执行的线程只能白白的浪费CPU时间，看着另一个线程拿着GIL欢快的执行着。然后达到切换时间后进入待调度状态，再被唤醒，再等待，以此往复恶性循环。

如何避免GIL影响
CPU密集型下的任务尽量采用多进程处理(multiprocessing).
如果你不想使用Cython解释器，就没有这个限制，同样很多Cython的特性你也放弃了。
利用 ctypes 绕过 GIL.ctypes会在调用C函数前释放GIL,可以通过ctypes和C动态库来让 python充分利用物理内核的计算能力。

作者：0行痴0
链接：https://www.jianshu.com/p/bc159d3054d1
來源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
"""