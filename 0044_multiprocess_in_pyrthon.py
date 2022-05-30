#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/10/18
import time

from multiprocessing import current_process

from multiprocessing import Process


def func():
    time.sleep(1)
    proc = current_process()
    print(proc.name, proc.pid)


def test_process():
    """
    这是在主进程中创建子进程，然后启动(start) 子进程，等待(join) 子进程执行完，再继续执行主进程的整个的执行流程。

那么，一个进程应该是用来做什么的，它应该保存一些什么状态，它的生命周期是什么样的呢？

一个进程需要处理一些不同任务，或者处理不同的对象。创建进程需要一个 function 和相关参数，参数可以是dict Process(target=func, args=(), kwargs = {})，name 可以用来标识进程。

控制子进程进入不同阶段的是 start(), join(), is_alive(), terminate(), exitcode 方法。这些方法只能在创建子进程的进程中执行。
    :return:
    """
    sub_proc = Process(target=func, args=())
    sub_proc.start()
    sub_proc.join()
    proc = current_process()
    print(proc.name, proc.pid)

test_process()


