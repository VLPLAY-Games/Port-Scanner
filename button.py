""" Файл для работы с кнопками"""

import logging
from raylib import colors

class Button:
    """ Класс для работы с кнопками"""
    def __init__(self):
        """ Инициализация """
        logging.info("Button class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("Button class deinitialized")

    def but_all_info(self, pr, task, language):
        """ Отрисовка и отработка кнопки вся информация """
        if pr.gui_button(
            pr.Rectangle(350, 100, 100, 50),
            'All info'):   
            task.task = 'all_info'
        pr.draw_rectangle_gradient_ex(pr.Rectangle(350, 100, 100, 50), colors.BLUE, colors.BLUE, colors.RED, colors.RED)
        pr.draw_text_ex(language.font, 'All info', pr.Vector2(370,115), 18, 1, colors.WHITE)

    def but_custom_task(self, pr, terminal, task, language):
        """ Отрисовка и отработка кнопки кастом """
        if pr.gui_button(
                pr.Rectangle(50, 200, 100, 50),
                'Start'):   
            terminal.draw_text = "Enter IP address to check: \n"
            terminal.terminal_active = True
            task.task = "ip_ports"
            task.status = "WAIT"
        pr.draw_rectangle_gradient_ex(pr.Rectangle(50, 200, 100, 50), colors.RED, colors.RED, colors.BLUE, colors.BLUE)
        pr.draw_text_ex(language.font, 'Start', pr.Vector2(70,215), 18, 1, colors.WHITE)

    def but_all_ports(self, pr, task, language):
        """ Отрисовка и обработка кнопки проверить все порты """
        # Получение открытых портов собственного IP
        if pr.gui_button(
                    pr.Rectangle(200, 100, 100, 50),
                    'Check all ports'):
            task.task = "all_ports"
        pr.draw_rectangle_gradient_ex(pr.Rectangle(200, 100, 100, 50), colors.RED, colors.RED, colors.BLUE, colors.BLUE)
        pr.draw_text_ex(language.font, 'Check all ports', pr.Vector2(205,115), 12, 1, colors.WHITE)

    def but_ip(self, ip, pr, terminal, app, task, language):
        """ Отрисовка и обработка кнопки получения всех ip """
        if pr.gui_button(
                    pr.Rectangle(50, 100, 100, 50),
                    'Check your IP'):
            terminal.draw_text = ip.get_all_ip(app, terminal, task)
            task.status = "OK"
            logging.info("Finished task 'get all ip'")
        pr.draw_rectangle_gradient_ex(pr.Rectangle(50, 100, 100, 50), colors.BLUE, colors.BLUE, colors.RED, colors.RED)
        pr.draw_text_ex(language.font, 'Check your IP', pr.Vector2(50,115), 14, 1, colors.WHITE)

    def but_next_console(self, pr, terminal, language):
        """ Отрисовка и обработка кнопки следующей страницы терминала """
        if pr.gui_button(
                    pr.Rectangle(950, 550, 25, 25),
                    '>>'):
            terminal.term_next()
        pr.draw_rectangle_gradient_ex(pr.Rectangle(950, 550, 25, 25), colors.BROWN, colors.BROWN, colors.DARKGRAY, colors.DARKGRAY)
        pr.draw_text_ex(language.font, '>>', pr.Vector2(960,560), 11, 1, colors.WHITE)

    def but_prev_console(self, pr, terminal, language):
        """ Отрисовка и обработка кнопки предыдущей страницы терминала """
        if pr.gui_button(
                    pr.Rectangle(900, 550, 25, 25),
                    '<<'):
            terminal.term_prev()
        pr.draw_rectangle_gradient_ex(pr.Rectangle(900, 550, 25, 25), colors.DARKGREEN, colors.DARKGREEN, colors.DARKBLUE, colors.DARKBLUE)
        pr.draw_text_ex(language.font, '<<', pr.Vector2(910,560), 11, 1, colors.WHITE)

    def but_lang_rus(self, pr, language):
        """ Отрисовка и обработка кнопки смены языка русский """
        if pr.gui_button(
                    pr.Rectangle(400, 50, 50, 25),
                    'Russian'):
            language.change_language(pr, "RU")
        pr.draw_rectangle_gradient_ex(pr.Rectangle(400, 50, 50, 25), colors.BROWN, colors.BROWN, colors.DARKGRAY, colors.DARKGRAY)
        pr.draw_text_ex(language.font, 'Russian', pr.Vector2(405,60), 11, 1, colors.WHITE)

    def but_lang_eng(self, pr, language):
        """ Отрисовка и обработка кнопки смены языка английский """
        if pr.gui_button(
                    pr.Rectangle(340, 50, 50, 25),
                    'English'):
            language.change_language(pr, "EN")
        pr.draw_rectangle_gradient_ex(pr.Rectangle(340, 50, 50, 25), colors.BROWN, colors.BROWN, colors.DARKGRAY, colors.DARKGRAY)
        pr.draw_text_ex(language.font, 'English', pr.Vector2(345,60), 11, 1, colors.WHITE)
    
    def but_info(self, pr, information, terminal, language):
        """ Отрисовка и обработка кнопки информации о функциях """
        if pr.gui_button(
                    pr.Rectangle(50, 500, 100, 50),
                    'Info'):
            terminal.draw_text = information.all_info_of_task
        pr.draw_rectangle_gradient_ex(pr.Rectangle(50, 500, 100, 50), colors.PURPLE, colors.PURPLE, colors.BLACK, colors.BLACK)
        pr.draw_text_ex(language.font, 'Info', pr.Vector2(70,515), 18, 1, colors.WHITE)

    def but_log(self, pr, terminal, language, log):
        """ Отрисовка и обработка кнопки отрисовки лога """
        if pr.gui_button(
                    pr.Rectangle(175, 500, 100, 50),
                    'Log'):
            terminal.draw_text = log.get_log()
        pr.draw_rectangle_gradient_ex(pr.Rectangle(175, 500, 100, 50), colors.PURPLE, colors.PURPLE, colors.BLACK, colors.BLACK)
        pr.draw_text_ex(language.font, 'Log', pr.Vector2(185,515), 18, 1, colors.WHITE)

    def check_all_but(self, ip, pr, terminal, task, app, language, information, log):
        """ Проверка всех кнопок """
        self.but_all_info(pr, task, language)
        self.but_custom_task(pr, terminal, task, language)
        self.but_ip(ip, pr, terminal, app, task, language)
        self.but_all_ports(pr, task, language)
        self.but_next_console(pr, terminal, language)
        self.but_prev_console(pr, terminal, language)
        self.but_lang_eng(pr,language)
        self.but_lang_rus(pr, language)
        self.but_info(pr, information, terminal, language)
        self.but_log(pr, terminal, language, log)
