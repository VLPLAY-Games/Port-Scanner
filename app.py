""" Файл для работы с приложением"""

import logging
from config import width, height, fps, app_name, version

class App():
    """ Основной класс приложения"""
    def __init__(self):
        """ Инициализация класса """
        self.version = version
        self.width = width
        self.height = height
        self.fps = fps
        self.app_name = app_name
        self.first_port = 0
        self.end_port = 0
        self.enter_pressed = False
        logging.info("App class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("App class deinitialized")

    def init_app(self, pr):
        """ Запуск приложения """
        try:
            pr.init_window(self.width, self.height, self.app_name)
            pr.set_target_fps(self.fps)
            pr.set_window_icon(pr.load_image('portscanner.png'))
            logging.info("App initialized")
        except Exception as e:
            logging.critical("Error while initializing App window: " + str(e))

    def draw_main(self, pr, colors, terminal, task):
        """ Отрисовка дизайна приложения """
        pr.draw_line(500,25,500,575,colors.BLACK)
        pr.draw_line(25,575,975,575,colors.BLACK)
        pr.draw_line(25,25,975,25,colors.BLACK)
        pr.draw_text("Select option", 50,50,25,colors.BLACK)
        pr.draw_text("Enter IP and ports", 50, 175, 15, colors.BLACK)
        terminal.draw_terminal(pr, colors, task)
        pr.draw_text(app_name + " by VL_PLAY Games " + version, 725, 585, 12, colors.BLACK)

    def error_init(self, e, pr, colors):
        """ Отрисовка ошибки """
        logging.critical(str(e) + version)
        pr.close_window()
        pr.init_window(300, 200, "Port Scanner Critical Error")
        pr.set_target_fps(30)
        pr.set_window_icon(pr.load_image('portscanner.png'))
        logging.info("Error window initialized")
        while not pr.window_should_close():
            pr.begin_drawing()
            pr.clear_background(colors.WHITE)
            pr.draw_text("Critical Error", 75, 75, 25, colors.BLACK)
            pr.draw_text("Check report.log", 25, 75, 25, colors.BLACK)
            pr.end_drawing()

    def exception(self, text, e, terminal, task):
        """ Обработка исключений """
        logging.error(text)
        logging.error(str(e))
        terminal.terminal_active = False
        task.task = ""
        self.enter_pressed = False
        terminal.draw_text += "An error has occurred"

    def fast_draw_text(self, text, pr, colors, terminal, task):
        """ Отрисовать перед выполнением задачи текст"""
        self.draw_main(pr, colors, terminal,task)
        pr.begin_drawing()
        pr.draw_text(text, 550, 125, 10, colors.BLACK)
        pr.clear_background(colors.WHITE)
        pr.end_drawing()
        pr.begin_drawing()
