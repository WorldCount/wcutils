#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

__author__ = 'WorldCount'


TOKEN = '217628569:AAEsYJ_Yl1FJXgjUqZeIJ08zWgwwkHcC7YI'
API = 'https://api.telegram.org/bot{token}/sendMessage?chat_id={user_id}&text={text}&parse_mode={parse_mode}'


# Отправляет сообщение в телеграмм
def send(message, uid, parse_mode=None):
    """
    :param message: Текст сообщения
    :param uid: ID пользователя
    :return: Статус отправки
    """
    url = API.format(token=TOKEN, user_id=uid, text=message, parse_mode=parse_mode)
    resp = requests.get(url)
    if resp.status_code != 200:
        return False
    return True
