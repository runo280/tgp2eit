# -*- coding: utf-8 -*-
import os


def is_offline():
    path = 'config.ini'
    return os.path.exists(path)


def delete_msg_file(file):
    if os.path.exists(file):
        os.remove(file)
