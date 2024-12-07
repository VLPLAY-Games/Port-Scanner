""" Файл для работы с кнопками"""

import logging
import colors

class Button:
    """ Класс для работы с кнопками"""
    def __init__(self):
        """ Инициализация """
        logging.info("Started Button class initializing")
        logging.info("Button class initialized successfully")

    def __del__(self):
        """ Деинициализация """
        logging.info("Button class deinitialized")

    def but_all_info(self, pr, task, language, settings):
        """ Отрисовка и отработка кнопки вся информация """
        if pr.gui_button(
            pr.Rectangle(355, 103, settings.but_width, settings.but_height),""):
            task.task = 'all_info'
        pr.draw_rectangle_rounded(pr.Rectangle(350, 100, 112, 62), 0.5, 5, colors.DARKGREEN)

        pr.draw_text_ex(language.font, language.get_text_tr("All info"), \
                        pr.Vector2(375, 120), settings.but_font_size, 1, colors.WHITE)

    def but_custom_task(self, pr, terminal, task, language, settings):
        """ Отрисовка и отработка кнопки кастом """
        if pr.gui_button(
                pr.Rectangle(55, 203, settings.but_width, settings.but_height), ""):
            terminal.draw_text = "Enter IP address to check: \n"
            terminal.terminal_active = True
            task.task = "ip_ports"
            task.status = "WAIT"
        pr.draw_rectangle_rounded(pr.Rectangle(50, 200, 112, 62), 0.5, 5, colors.DARKBYZAN)
        pr.draw_text_ex(language.font, language.get_text_tr('Custom IP'),\
                         pr.Vector2(65, 215), settings.but_font_size, 1, colors.WHITE)
        pr.draw_text_ex(language.font, language.get_text_tr('and ports'),\
                         pr.Vector2(68, 230), settings.but_font_size, 1, colors.WHITE)

    def but_all_ports(self, pr, task, language, settings):
        """ Отрисовка и обработка кнопки проверить все порты """
        # Получение открытых портов собственного IP
        if pr.gui_button(
                    pr.Rectangle(205, 103, settings.but_width, settings.but_height), ""):
            task.task = "all_ports"
        pr.draw_rectangle_rounded(pr.Rectangle(200, 100, 112, 62), 0.5, 5, colors.DARKPURPLE)
        pr.draw_text_ex(language.font, language.get_text_tr('Check all'),\
                         pr.Vector2(220, 116), settings.but_font_size, 1, colors.WHITE)
        pr.draw_text_ex(language.font, language.get_text_tr('ports'),\
                         pr.Vector2(235, 131), settings.but_font_size, 1, colors.WHITE)

    def but_ip(self, ip, pr, terminal, app, task, language, settings):
        """ Отрисовка и обработка кнопки получения всех ip """
        if pr.gui_button(
                    pr.Rectangle(55, 103, settings.but_width, settings.but_height), ""):
            terminal.draw_text = ""
            for res in ip.get_all_ip(app, terminal, task):
                terminal.draw_text += res + '\n'
            task.status = "OK"
            logging.info("Finished task 'get all ip'")
        pr.draw_rectangle_rounded(pr.Rectangle(50, 100, 112, 62), 0.5, 5, colors.DARKRED)
        pr.draw_text_ex(language.font, language.get_text_tr('Check your'), \
                        pr.Vector2(60, 117), settings.but_font_size, 1, colors.WHITE)
        pr.draw_text_ex(language.font, language.get_text_tr('IP'), \
                        pr.Vector2(100, 132), settings.but_font_size, 1, colors.WHITE)

    def but_next_console(self, pr, terminal, language):
        """ Отрисовка и обработка кнопки следующей страницы терминала """
        if pr.gui_button(
                    pr.Rectangle(952, 551, 20, 20), ""):
            terminal.term_next()
        pr.draw_rectangle_rounded(pr.Rectangle(950, 550, 25, 25), 0.5, 5, colors.AQUA)
        pr.draw_text_ex(language.font, language.get_text_tr('>>'), \
                        pr.Vector2(957, 558), 11, 1, colors.WHITE)

    def but_prev_console(self, pr, terminal, language):
        """ Отрисовка и обработка кнопки предыдущей страницы терминала """
        if pr.gui_button(
                    pr.Rectangle(902, 551, 20, 20), ""):
            terminal.term_prev()
        pr.draw_rectangle_rounded(pr.Rectangle(900, 550, 25, 25), 0.5, 5, colors.AQUA)
        pr.draw_text_ex(language.font, language.get_text_tr('<<'), \
                        pr.Vector2(907, 558), 11, 1, colors.WHITE)

    def but_lang_rus(self, pr, language, settings):
        """ Отрисовка и обработка кнопки смены языка русский """
        if pr.gui_button(
                    pr.Rectangle(403, 53, 45, 20), ""):
            language.change_language(pr, "RU", settings)
        pr.draw_rectangle_rounded(pr.Rectangle(400, 50, 50, 25), 0.5, 5, colors.DARKGREENBLUE)
        pr.draw_text_ex(language.font, language.get_text_tr('Russian'),
                        pr.Vector2(405, 58), 11, 1, colors.WHITE)

    def but_lang_eng(self, pr, language, settings):
        """ Отрисовка и обработка кнопки смены языка английский """
        if pr.gui_button(
                    pr.Rectangle(343, 53, 45, 20), ""):
            language.change_language(pr, "EN", settings)
        pr.draw_rectangle_rounded(pr.Rectangle(340, 50, 50, 25), 0.5, 5, colors.DARKGREENBLUE)
        pr.draw_text_ex(language.font, language.get_text_tr('English'), \
                        pr.Vector2(347, 58), 11, 1, colors.WHITE)

    def but_help(self, pr, terminal, language, settings):
        """ Отрисовка и обработка кнопки информации о функциях """
        if pr.gui_button(
                    pr.Rectangle(53, 528, 55, 25), ""):
            terminal.draw_text = settings.info
        pr.draw_rectangle_rounded(pr.Rectangle(50, 525, 60, 30), 0.5, 5, colors.DARKBLUE)
        pr.draw_text_ex(language.font, language.get_text_tr('Help'), \
                        pr.Vector2(63, 533), 16, 1, colors.WHITE)

    def but_log(self, pr, terminal, language, log):
        """ Отрисовка и обработка кнопки отрисовки лога """
        if pr.gui_button(
                    pr.Rectangle(128, 528, 55, 25), ""):
            terminal.draw_text = log.get_log(True)
        pr.draw_rectangle_rounded(pr.Rectangle(125, 525, 60, 30), 0.5, 5, colors.DARKBLUE)
        pr.draw_text_ex(language.font, language.get_text_tr('Log'), \
                        pr.Vector2(140, 532), 16, 1, colors.WHITE)

    def but_clear(self, pr, terminal, language):
        """ Отрисовка и обработка кнопки отрисовки очистки терминала """
        if pr.gui_button(
                    pr.Rectangle(203, 528, 55, 25), ""):
            terminal.draw_text = ""
        pr.draw_rectangle_rounded(pr.Rectangle(200, 525, 60, 30), 0.5, 5, colors.DARKBLUE)
        pr.draw_text_ex(language.font, language.get_text_tr('Clear'), \
                        pr.Vector2(213, 532), 16, 1, colors.WHITE)

    def but_settings(self, pr, language, settings):
        """ Отрисовка и обработка кнопки отрисовки очистки терминала """
        if pr.gui_button(
                    pr.Rectangle(278, 528, 55, 25), ""):
            settings.settings_window(pr)
        pr.draw_rectangle_rounded(pr.Rectangle(275, 525, 60, 30), 0.5, 5, colors.DARKBLUE)
        pr.draw_text_ex(language.font, language.get_text_tr('Settings'), \
                        pr.Vector2(275, 532), 16, 1, colors.WHITE)

    def but_ping(self, pr, terminal, language, task, settings):
        """ Отрисовка и обработка кнопки пинга """
        if pr.gui_button(
                    pr.Rectangle(205, 203, settings.but_width, settings.but_height), ""):
            terminal.draw_text = "Enter IP or link to ping: \n"
            terminal.terminal_active = True
            task.task = "ping_start"
            task.status = "WAIT"
            logging.info("Ping command started")
        pr.draw_rectangle_rounded(pr.Rectangle(200, 200, 112, 62), 0.5, 5, colors.DARKORANGE)
        pr.draw_text_ex(language.font, language.get_text_tr('Ping'), \
                        pr.Vector2(235, 220), settings.but_font_size, 1, colors.WHITE)

    def but_terminal(self, pr, terminal, language, task, settings):
        """ Отрисовка и обработка кнопки кастомного терминала"""
        if pr.gui_button(
                    pr.Rectangle(355, 203, settings.but_width, settings.but_height), ""):
            terminal.draw_text = "Enter command: \n"
            terminal.terminal_active = True
            task.task = "cus_terminal"
            task.status = "WAIT"
            logging.info("Custom terminal command started")
        pr.draw_rectangle_rounded(pr.Rectangle(350, 200, 112, 62), 0.5, 5, colors.DARKAQUA)
        pr.draw_text_ex(language.font, language.get_text_tr('Terminal'), \
                        pr.Vector2(370, 222), settings.but_font_size, 1, colors.WHITE)

    def but_active_devices(self, pr, terminal, language, task, settings):
        """ Отрисовка и обработка кнопки проверки активных устройств в сети"""
        if pr.gui_button(
                    pr.Rectangle(55, 303, settings.but_width, settings.but_height), ""):
            terminal.draw_text = "Enter command: \n"
            terminal.terminal_active = True
            task.task = "act_devices"
            task.status = "WAIT"
            logging.info("Active devices command started")
        pr.draw_rectangle_rounded(pr.Rectangle(50, 300, 112, 62), 0.5, 5, colors.DARKGREENORANGE)
        pr.draw_text_ex(language.font, language.get_text_tr('Active'), \
                        pr.Vector2(80, 313), settings.but_font_size, 1, colors.WHITE)
        pr.draw_text_ex(language.font, language.get_text_tr('devices'), \
                        pr.Vector2(75, 328), settings.but_font_size, 1, colors.WHITE)

    def check_all_but(self, ip, pr, terminal, task, app, language, log, settings):
        """ Проверка всех кнопок """
        self.but_all_info(pr, task, language, settings)
        self.but_custom_task(pr, terminal, task, language, settings)
        self.but_ip(ip, pr, terminal, app, task, language, settings)
        self.but_all_ports(pr, task, language, settings)
        self.but_next_console(pr, terminal, language)
        self.but_prev_console(pr, terminal, language)
        self.but_lang_eng(pr, language, settings)
        self.but_lang_rus(pr, language, settings)
        self.but_help(pr, terminal, language, settings)
        self.but_log(pr, terminal, language, log)
        self.but_settings(pr, language, settings)
        self.but_ping(pr, terminal, language, task, settings)
        self.but_clear(pr, terminal, language)
        self.but_terminal(pr, terminal, language, task, settings)
        self.but_active_devices(pr, terminal, language, task, settings)
