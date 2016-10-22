#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import socket
import subprocess


__author__ = 'WorldCount'


"""
Различные утилиты для работы с сетью
"""


# Возвращает хеш-сумму пароля
def password_to_hash(password):
    md5 = hashlib.md5(password.encode())
    return md5.hexdigest()


# Возвращает IP-адрес компьютера
def get_ip_address():
    return socket.gethostbyname(socket.gethostname())


# Возвращает имя компьютера
def get_host_name():
    return socket.gethostname()


# Возвращает статус сервера или сайта
def ping(ip):
    pipe = subprocess.Popen(['ping', '-n', '1', '-w', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            shell=True)
    response = pipe.communicate()[0].decode('cp866')
    if 'TTL' in response:
        return True
    return False
