#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

__author__ = 'WorldCount'


# Форматирует дату
def format_date(date):
    if type(date) == datetime.datetime:
        return date.strftime("%d.%m.%Y %H:%M:%S")
    return False
