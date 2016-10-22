#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


__author__ = 'WorldCount'


"""
Разные утилиты для работы с файлами
"""


# Создает директории из списка
def create_dirs(list_dirs):
    if type(list_dirs) == list:
        for new_dir in list_dirs:
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
        return True
    return False


# Возвращает путь к папке файла
def get_file_dir(path):
    return os.path.dirname(path)
