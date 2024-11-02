""" Файл для работы с логами"""
import logging
class Log:
    """ Класс для работы с логами"""
    def __init__(self):
        """ Инициализация """
        logging.info("Log class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("Log class deinitialized")
