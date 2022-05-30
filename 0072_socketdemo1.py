#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/8/17


import socket

import errno

address = ('', 20000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(address)

sock.listen(100)


def io_block():
    """
    io阻塞模型
    :return:
    """
    while True:
        conn, addr = sock.accept()
        print('client {} connect'.format(conn.fileno()))
        while True:
            data = conn.recv(1024)
            if not  data:
                print('client {} closed'.format(conn.fileno()))
                break
            else:
                print('data is ', data)
                conn.sendall(data)
                conn.close()
                break
        conn.close()

def io_no_block():
    while True:
        try:
            conn, addr = sock.accept()
        except socket.error as e:
            if e.args[0] in (errno.EWOULDBLOCK, errno.EAGAIN):
                continue
            else:
                raise
        print('client {} connect'.format(conn.fileno()))
        conn.setblocking(False)
        while True:
            try:
                data = conn.recv(1024)
            except socket.error as e :
                if e.args[0] in (errno.EWOULDBLOCK, errno.EAGAIN):
                    continue
                else:
                    raise
            if not data:
                print('client {} closed'.format(conn.fileno()))
                break
            else:
                print('data is ', data)
                conn.sendall(data)
                conn.close()
                # break
    conn.close

io_no_block()