""" Файл для работы с терминалом"""

import logging

class Terminal:
    """ Класс для работы с Терминалом """
    def __init__(self):
        """ Инициализация """
        self.page = 0
        self.draw_text = ""
        self.terminal_active = False
        self.pages = 0
        self.temp = ""
        logging.info("Terminal class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("Terminal class deinitialized")

    def draw_terminal(self, pr, colors, task, language):
        """ Отрисовка дизайна терминала """
        self.temp = "Result "
        if task.status == "WORK":
            self.temp += "(Working)"
        elif task.status == "OK":
            self.temp += "(Complete)"
        elif task.status == "ERR":
            self.temp += "(Error)"
        elif task.status == "WAIT":
            self.temp += "(Wait input)"
        pr.draw_text_ex(language.font, self.temp, pr.Vector2(550,50), 25, 1, colors.WHITE)
        pr.draw_rectangle_lines(525, 100, 450, 450, colors.WHITE)

    def term_prev(self):
        """ Предыдущая страница """
        if self.page > 0:
            self.page += 1

    def term_next(self):
        """ Следующая страница """
        if self.page < self.pages:
            self.page -= 1

    def draw_terminal_text(self, keys, pr, colors, language):
        """ Отрисовка терминала """
        self.draw_text = str(self.check_text())
        temp = 0
        arr = []
        temp_str = ""
        for string in self.draw_text.split(sep="\n"):
            temp_str += string + "\n"
            if temp > 20:
                arr.append(temp_str)
                temp_str = ""
                temp = 0
            temp += 1
        if temp <= 20:
            arr.append(temp_str)
        self.pages = len(arr)
        if len(arr) != 0:
            pr.draw_text_ex(language.font, str(arr[self.page]) + str(''.join(keys)) if self.terminal_active \
                        else str(arr[self.page]), \
                        pr.Vector2(550, 125), 12, 1, colors.WHITE)

    def check_text(self):
        """ Проверка переноса строки"""
        temp = ""
        temp_count = 0
        for string in self.draw_text:
            for letter in string:
                if letter != "\n":
                    temp_count += 1
                    if temp_count > 75:
                        temp += "\n"
                        temp_count = 0
                else:
                    temp_count = 0
                temp += letter
        return temp

