#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/8/23
import re
import socket
import threading
import time

from pip._vendor.distlib.compat import raw_input

"""
1.单工版非常简单，只能客户端单方面向服务端发消息，服务端回复固定模板消息。
2.半双工实现是连接建立以后，服务器等待客户端发送消息，客户端发送消息后等待接收服务器，这样一来一回循环往复下去。直到出现quit，关闭连接。
3.全双工。因为TCP连接是一个流，所以Socket模块的recv()是直到Scoket连接终断不会停止等待接受从另一端发送的消息的。
全双工实现比半双工工多了个线程处理，所以服务器与客户端必须开两个线程，一个收消息一个发消息，并且发消息的线程需要阻塞收消息的线程。

"""


def server01():
    """
    socket编程单向server端
    :return:
    """

    def tcplink(sock, addr):
        print('Access new connection from {}'.format(addr))
        sock.send('Welcome!')
        while True:
            data = sock.recv(1024)
            print(data)
            time.sleep(1)
            if not data or data == 'exit':
                break
            sock.send('Hello, {}'.format(addr))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print('Waiting for connection....')
    while True:
        # 接受一个新连接
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


def server02():
    """
    半双工实现
    :return:
    """
    host = '127.0.0.1'
    port = 50001
    busize = 1024
    addr = (host, port)

    def closetcnt(s):
        s.close()
        print("Session closing")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(addr)
    s.listen(1)
    try:
        while True:
            print("waiting for connecting....")
            ts, caddr = s.accept()
            print("...connection from :{}".format(caddr))
            try:
                while True:
                    rdata = ts.recv(busize)
                    if not rdata:
                        continue
                    elif rdata == 'quit':
                        break
                    else:
                        print("from {}  {} \n {}".format(caddr[0], time.ctime(), rdata))
                    while True:
                        sdata = str(input('> '))
                        if not sdata:
                            break
                        else:
                            ts.send("from {}  {} \n {}".format(caddr[0], time.ctime(), sdata))
                            break

            except socket.error as  detail:
                print(detail)
            closetcnt(ts)

    finally:
        s.close


def server03():
    """
    全双工
    :return:
    """
    host = '127.0.0.1'
    port = 50002
    bufsize = 1024
    addr = (host, port)

    ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ts.bind(addr)
    ts.listen(5)

    clients = {}  # username ->socket
    chatwith = {}  # user1.socket->user2.socket

    """
    clients中记录了连接的客户端的用户名和套接字的对应关系
    chantwith中记录了通信双方的套接字的对应
    文本只有四种类型：None，Quit, To：someone，其他文本
    """

    def messagetransform(sock, user):
        while True:
            data = sock.recv(bufsize)
            if not data:
                if sock in chatwith:
                    data = '{}.'.format(data)
                    chatwith[sock].send(data)
                    chatwith.pop(chatwith[sock])
                    chatwith.pop(sock)
                clients.pop(user)
                break
            if data == "Quit":
                sock.send(data)
                if sock in chatwith:
                    data = "{}.".format(data)
                    chatwith[sock].send(data)
                    chatwith.pop(chatwith[sock])
                    chatwith.pop(sock)
                clients.pop(user)
                sock.close()
                break
            elif re.match('To:.+', data) is not None:
                data = data[3:]
                if data in clients:
                    if data == user:
                        sock.send(b'please dont try to talk with yourself.')
                    else:
                        chatwith[sock] = clients[user]
                        chatwith[clients[data]] = sock
                else:
                    sock.send(b'the user {} is not exits'.format(data))

            else:
                if sock in chatwith:
                    chatwith[sock].send('[{}] [{}] ({})'.format(time.ctime(), user, data))
                else:
                    sock.send('Nobody is chating with you. Maybe the one talked with you is '
                              'talking with someone else')

    def connect_thread(sock, test):  # 客户端sockct
        """
        每个客户端连接以后，都会启动一个新的线程
        连接成功后需要输入用户名
        输入的用户名可能会：已存在，客户端直接输入ctrl+c退出，合法用户米
        :return:
        """

        user = None
        while True:
            username = sock.recv(bufsize)
            if not username:
                print('The client logout without input a name')
                break
            if username in clients:
                sock.send(b'Reuse')
            else:
                sock.send(b'OK')
                clients[username] = sock  # username -> sock
                user = username
                break
        if not user:
            sock.close()
            return
        print('The username is {}'.format(user))
        messagetransform(sock, user)

    while True:
        print('...waiting for connection')
        s, addr = ts.accept()
        print('connected from:{}'.format(addr))
        chat = threading.Thread(target=connect_thread, args=(s,None))
        chat.start()


server03()
