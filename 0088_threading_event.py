#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/9/18
import threading

a_event = threading.Event()
b_event = threading.Event()
c_event = threading.Event()
d_event = threading.Event()


def print_a(event, next_event):
    for i in range(3):
        event.wait()
        print("a{}".format(i))
        event.clear()
        next_event.set()


def print_b(event, next_event):
    for i in range(3):
        event.wait()
        print("b{}".format(i))
        event.clear()
        next_event.set()


def print_c(event, next_event):
    for i in range(3):
        event.wait()
        print("c{}".format(i))
        event.clear()
        next_event.set()


def print_d(event, next_event):
    for i in range(3):
        event.wait()
        print("d{}".format(i))
        event.clear()
        next_event.set()


a_thread = threading.Thread(target=print_a, args=(a_event, b_event))
b_thread = threading.Thread(target=print_b, args=(b_event, c_event))
c_thread = threading.Thread(target=print_c, args=(c_event, d_event))
d_thread = threading.Thread(target=print_d, args=(d_event, a_event))

a_thread.start()
b_thread.start()
c_thread.start()
d_thread.start()

a_event.set()
