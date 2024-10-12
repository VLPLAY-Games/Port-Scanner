import logging


class Button:
    """ Класс для работы с кнопками"""
    def __init__(self):
        """ Инициализация """
        logging.info("Button class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("Button class deinitialized")

    def but_all_info(self, app, pr, task):
        """ Отрисовка и отработка кнопки вся информация """
        if pr.gui_button(
                pr.Rectangle(350, 100, 100, 50),
                'All info'):   
            task.task = 'all_info'

    def but_custom_task(self, app, pr, terminal, task):
        """ Отрисовка и отработка кнопки кастом """
        if pr.gui_button(
                pr.Rectangle(50, 200, 100, 50),
                'Start'):   
            terminal.draw_text = "Enter IP address to check: \n"
            terminal.terminal_active = True
            task.task = "ip_ports"

    def but_main_ports(self, app, ip, port, pr, colors, task):
        """ Отрисовка и обработка кнопки проверить основные порты """
        # Получение открытых портов собственного IP
        if pr.gui_button(
                    pr.Rectangle(200, 100, 100, 50),
                    'Check all ports'):
            task.task = "all_ports"
            

    def but_ip(self, ip, pr, terminal):
        """ Отрисовка и обработка кнопки получения всех ip """
        if pr.gui_button(
                    pr.Rectangle(50, 100, 100, 50),
                    'Check your IP'):
            terminal.draw_text = ip.get_all_ip()

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

    def check_all_but(self, app, ip, port, pr, colors, terminal, task):
        """ Проверка всех кнопок """
        self.but_all_info(app, pr, task)
        self.but_custom_task(app, pr, terminal, task)
        self.but_ip(ip, pr, terminal)
        self.but_main_ports(app, ip, port, pr, colors, task)
        self.but_next_console(pr, terminal)
        self.but_prev_console(pr, terminal)