#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'wang.zhiqiang'

import threading
import time


def tstart():
    print('t start...')
    time.sleep(2)
    print('t end...')


con = threading.Condition()
word = range(100)


def work():
    global word
    con.acquire()
    while True:
        print(word[0])
        word = word[1:]
        if len(word) == 0:
            break
        con.notify()
        if len(word) == 1:
            break
        con.wait()
    con.release()


t1 = threading.Thread(target=work)
t2 = threading.Thread(target=work)
t1.start()
t2.start()
t1.join()
t2.join()
