""" Файл для работы с клавиатурой """
import logging
from pyperclip import paste
from collections import deque

class Keyboard:
    """ Класс для работы с клавиатурой"""
    
    def __init__(self):
        """ Инициализация """
        logging.info("Started Keyboard class initializing")
        self.keys = deque()
        self.enter_pressed = False
        logging.info("Keyboard class initialized successfully")

    def del_keys(self):
        """ Деинициализация """
        logging.info("Keyboard class deinitialized")

    def get_keys(self):
        """ Получить текст с клавиатуры """
        return ''.join(self.keys)

    def append_keys(self, var):
        """ Добавить текст """
        self.keys.append(var)

    def keys_erase(self):
        """ Очистить клавиатуру """
        self.keys.clear()

    def keys_del(self):
        """ Удалить 1 символ с конца"""
        if self.keys:
            self.keys.pop()

    def check_key(self, pr, terminal):
        """ Добавление текста с клавиатуры """
        while value := pr.get_key_pressed():
            if terminal.terminal_active:
                enter_pressed = pr.is_key_pressed(257)
                key_del_pressed = pr.is_key_pressed(259)
                paste_pressed = pr.is_key_down(341) or pr.is_key_down(345)
                shift_pressed = pr.is_key_down(340) or pr.is_key_down(344)

                if enter_pressed:
                    self.enter_pressed = True
                elif key_del_pressed:
                    self.keys_del()
                elif paste_pressed and chr(value) == 'V':
                    self.keys.extend(list(paste()))
                
                else:
                    char_to_add = chr(value).lower() if not shift_pressed else chr(value)
                    if (32 <= value <= 126):
                        self.keys.append(char_to_add)
