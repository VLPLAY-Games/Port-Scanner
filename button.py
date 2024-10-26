""" Файл для работы с кнопками"""

import logging

class Button:
    """ Класс для работы с кнопками"""
    def __init__(self):
        """ Инициализация """
        logging.info("Button class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("Button class deinitialized")

    def but_all_info(self, pr, task):
        """ Отрисовка и отработка кнопки вся информация """
        if pr.gui_button(
                pr.Rectangle(350, 100, 100, 50),
                'All info'):   
            task.task = 'all_info'

    def but_custom_task(self, pr, terminal, task):
        """ Отрисовка и отработка кнопки кастом """
        if pr.gui_button(
                pr.Rectangle(50, 200, 100, 50),
                'Start'):   
            terminal.draw_text = "Enter IP address to check: \n"
            terminal.terminal_active = True
            task.task = "ip_ports"
            task.status = "WAIT"

    def but_all_ports(self, pr, task):
        """ Отрисовка и обработка кнопки проверить все порты """
        # Получение открытых портов собственного IP
        if pr.gui_button(
                    pr.Rectangle(200, 100, 100, 50),
                    'Check all ports'):
            task.task = "all_ports"

    def but_ip(self, ip, pr, terminal, app, task):
        """ Отрисовка и обработка кнопки получения всех ip """
        if pr.gui_button(
                    pr.Rectangle(50, 100, 100, 50),
                    'Check your IP'):
            terminal.draw_text = ip.get_all_ip(app, terminal, task)
            task.status = "OK"
            logging.info("Finished task 'get all ip'")

    def but_next_console(self, pr, terminal):
        """ Отрисовка и обработка кнопки следующей страницы терминала """
        if pr.gui_button(
                    pr.Rectangle(950, 550, 25, 25),
                    '>>'):
            terminal.term_next()

    def but_prev_console(self, pr, terminal):
        """ Отрисовка и обработка кнопки предыдущей страницы терминала """
        if pr.gui_button(
                    pr.Rectangle(900, 550, 25, 25),
                    '<<'):
            terminal.term_prev()

    def but_lang_rus(self, pr, language):
        """ Отрисовка и обработка кнопки смены языка русский """
        if pr.gui_button(
                    pr.Rectangle(400, 50, 50, 25),
                    'Russian'):
            language.change_language(pr, "RU")

    def but_lang_eng(self, pr, language):
        """ Отрисовка и обработка кнопки смены языка английский """
        if pr.gui_button(
                    pr.Rectangle(340, 50, 50, 25),
                    'English'):
            language.change_language(pr, "EN")

    def check_all_but(self, ip, pr, terminal, task, app, language):
        """ Проверка всех кнопок """
        self.but_all_info(pr, task)
        self.but_custom_task(pr, terminal, task)
        self.but_ip(ip, pr, terminal, app, task)
        self.but_all_ports(pr, task)
        self.but_next_console(pr, terminal)
        self.but_prev_console(pr, terminal)
        self.but_lang_eng(pr,language)
        self.but_lang_rus(pr, language)
