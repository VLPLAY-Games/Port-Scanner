""" Файл для работы с терминалом"""

import logging
from subprocess import check_output
import colors

class Terminal:
    """ Класс для работы с Терминалом """
    def __init__(self):
        """ Инициализация """
        logging.info("Started Terminal class initializing")
        self.page = 0
        self.draw_text = ""
        self.terminal_active = False
        self.pages = 0
        self.temp = ""
        self.arr_text = []
        self.custom_task = ""
        logging.info("Terminal class initialized successfully")

    def __del__(self):
        """ Деинициализация """
        logging.info("Terminal class deinitialized")

    def draw_terminal(self, pr, task, language):
        """ Отрисовка дизайна терминала """
        self.temp = language.get_text_tr("Result ")
        if task.status == "WORK":
            self.temp += language.get_text_tr("(Working)")
        elif task.status == "OK":
            self.temp += language.get_text_tr("(Complete)")
        elif task.status == "ERR":
            self.temp += language.get_text_tr("(Error)")
        elif task.status == "WAIT":
            self.temp += language.get_text_tr("(Wait input)")
        pr.draw_text_ex(language.font, self.temp, pr.Vector2(550,50), 25, 1, colors.WHITE)
        pr.draw_rectangle_lines(525, 100, 450, 450, colors.WHITE)

    def term_prev(self):
        """ Предыдущая страница """
        if self.page > 0:
            self.page -= 1

    def term_next(self):
        """ Следующая страница """
        if self.page < self.pages - 1:
            self.page += 1

    def draw_terminal_text(self, keys, pr, language):
        """ Отрисовка терминала """
        self.draw_text = str(self.check_text())
        self.check_pages()
        self.pages = len(self.arr_text)
        if len(self.arr_text) != 0:
            pr.draw_text_ex(language.english_font, str(self.arr_text[self.page]) + \
                            str(''.join(keys)) if self.terminal_active else \
                            str(self.arr_text[self.page]), \
                            pr.Vector2(550, 125), 12, 1, colors.WHITE)

    def check_text(self, text=""):
        """ Проверка переноса строки"""
        temp = []
        temp_count = 0
        if text == "":
            text = self.draw_text
        for string in text:
            for letter in string:
                if 32 <= ord(letter) <= 126 or letter == "\n":
                    if letter != "\n":
                        temp_count += 1
                        if temp_count > 68:
                            temp.append("\n")
                            temp_count = 1
                    else:
                        temp_count = 0
                    temp.append(letter)
        return ''.join(temp)


    def check_pages(self):
        """ Проверка на несколько страниц"""
        self.arr_text = []
        temp_str = []

        for string in self.draw_text.split(sep="\n"):
            temp_str.append(string)

            if len(temp_str) >= 28:
                self.arr_text.append("\n".join(temp_str))
                temp_str = []

        if temp_str:
            self.arr_text.append("\n".join(temp_str))

    def custom_terminal(self):
        """ Кастомная задача """
        try:
            self.draw_text += check_output(self.custom_task.lower(), \
                                                      shell=True).decode("utf-8")
            logging.info("Custom terminal task command completed")
        except Exception as e:
            self.draw_text += str(e)
            logging.error("Command execution error: %s", str(e))
