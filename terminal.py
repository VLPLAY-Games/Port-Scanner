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

    def draw_terminal(self, pr, colors, task):
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
        pr.draw_text(self.temp, 550,50,25,colors.BLACK)
        pr.draw_rectangle_lines(525, 100, 450, 450, colors.BLACK)

    def term_prev(self):
        """ Предыдущая страница """
        pass

    def term_next(self):
        """ Следующая страница """
        pass

    def draw_terminal_text(self, keys, pr, colors):
        """ Отрисовка терминала """
        self.draw_text = self.check_text()
        pr.draw_text(self.draw_text + str(''.join(keys)) if self.terminal_active \
                    else self.draw_text, \
                    550, 125, 10, colors.BLACK)

    def check_text(self):
        """ Проверка переноса строки и 2 страницы"""
        temp = ""
        temp_count = 0
        for string in self.draw_text:
            for letter in string:
                if letter != "\n":
                    temp_count += 1
                    if temp_count > 80:
                        temp += "\n"
                        temp_count = 0
                else:
                    temp_count = 0
                temp += letter
        return temp
