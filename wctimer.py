#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit


__author__ = 'WorldCount'


"""
Измерение скорости выполнения
"""


# Декоратор для измерения скорости выполнения
def get_time_exec(func):
    def wrapper():
        with WCTimer(True):
            return func()
    return wrapper


# Время выполнения
class WCTimer(object):

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.start = ''
        self.end = ''
        self.secs = ''

    def __enter__(self):
        self.start = timeit.default_timer()
        return self

    def __exit__(self, *args):
        self.end = timeit.default_timer()
        self.secs = self.end - self.start

        if self.verbose:
            print("Затраченное время: %.7s сек.\n" % self.secs)
