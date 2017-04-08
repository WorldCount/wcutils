#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob


__author__ = 'WorldCount'


"""
Разные утилиты для работы с файлами
"""


# Создает директории из списка
def create_dirs(list_dirs):
    """
    :param list_dirs: Список директорий
    :return: Результат работы
    """
    if type(list_dirs) == list:
        for new_dir in list_dirs:
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
        return True
    return False


# Возвращает путь к папке файла
def get_file_dir(path):
    """
    :param path: Путь к файлу
    :return: Путь к папке
    """
    return os.path.abspath(os.path.dirname(path))


# Ищет файлы в папке
def find_files(path_to_dir, ext='*.*F'):
    """
    :param path_to_dir: Путь до папки
    :param ext: Расширения файлов
    :return: Список файлов
    """
    files = glob.glob(os.path.join(path_to_dir, ext))
    return files
