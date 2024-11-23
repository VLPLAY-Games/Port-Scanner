""" Файл для работы с клавиатурой"""

import logging


class Keyboard:
    """ Класс для работы с клавиатурой"""
    def __init__(self):
        """ Инициализация """
        logging.info("Started Keyboard class initializing")
        self.keys = []
        self.enter_pressed = False
        logging.info("Keyboard class initialized successfully")

    def __del__(self):
        """ Деинициализация """
        logging.info("Keyboard class deinitialized")

    def get_keys(self):
        """ Получить текст с клавиатуры """
        return self.keys

    def append_keys(self, var):
        """ Добавить текст """
        self.keys.append(var)

    def keys_erase(self):
        """ Очистить клавиатуру """
        self.keys = []

    def keys_del(self):
        """ Удалить 1 смивол с конца"""
        self.keys = self.keys[:-1]

    def check_key(self, pr, terminal):
        """ Добавление текста с клавиатуры """
        # Получение нажатия всех кнопок с клавиатуры
        while value := pr.get_key_pressed():
            if terminal.terminal_active:
                if pr.is_key_pressed(257):
                    self.enter_pressed = True
                elif pr.is_key_pressed(259):
                    self.keys_del()
                else:
                    if (pr.is_key_down(340) or pr.is_key_down(344)):
                        if (value >= 65 and value <= 90) or (chr(value) >= '0' \
                                                             and chr(value) <= '9'):
                            self.keys.append(chr(value))
                    else:
                        self.keys.append(chr(value).lower())
