#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


__author__ = 'WorldCount'


"""
Консольные утилиты
"""


# Функция отрисовки прогрессбара
def print_progress(iteration, total, prefix='', suffix='', decimals=1, bar_length=100):
    """
    :param iteration: Текущая итерация
    :param total:  Всего итерация
    :param prefix: Префикс сообщения
    :param suffix: Суффикс сообщения
    :param decimals:
    :param bar_length: Длина бара
    :return: None
    """
    format_str = "{0:." + str(decimals) + "f}"
    percents = format_str.format(100 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()
