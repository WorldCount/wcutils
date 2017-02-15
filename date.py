#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

__author__ = 'WorldCount'


# Форматирует дату
def format_date(in_date):
    if type(in_date) == datetime.datetime:
        return in_date.strftime("%d.%m.%Y %H:%M:%S")
    elif type(in_date) == datetime.date:
        return in_date.strftime("%d.%m.%Y")
    return False