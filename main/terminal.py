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
        pass

    def term_next(self):
        """ Следующая страница """
        pass

    def draw_terminal_text(self, keys, pr, colors, language):
        """ Отрисовка терминала """
        self.draw_text = self.check_text()
        pr.draw_text_ex(language.font, self.draw_text + str(''.join(keys)) if self.terminal_active \
                    else self.draw_text, \
                    pr.Vector2(550, 125), 12, 1, colors.WHITE)

    def check_text(self):
        """ Проверка переноса строки и 2 страницы"""
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

