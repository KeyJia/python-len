#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/17 15:03
# @Author: KeyJia
# @File: decorator.py

import time
def timmer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print('the func run time is %s' %(stop_time-start_time) )
    return warpper

@timmer
def test1():
    time.sleep(3)
    print('in the test1')
test1()