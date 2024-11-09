""" Файл для работы с логами"""
import logging
import os
from raylib import colors
class Log:
    """ Класс для работы с логами"""
    def __init__(self):
        """ Инициализация """
        self.temp = 0
        self.log_lines = []
        self.log = []
        self.is_drawed = False
        self.temp = open("report.log", "a")
        self.temp.close()
        os.remove("report.log")
        # Логирование приложения
        logging.basicConfig(filename='report.log', \
                    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
        logging.info("             Port scanner                 ")
        logging.info("App started")
        logging.info("Log class initialized")


    def __del__(self):
        """ Деинициализация """
        logging.info("Log class deinitialized")

    def get_log(self, terminal = False):
        """ Получение лога"""
        if (self.is_drawed == False):
            self.log = []
            self.log_lines = []
            with open("report.log") as file:
                self.log_lines = [line.rstrip() for line in file]
            for line in self.log_lines:
                self.log.append(line + '\n')
            if (terminal == False):
                self.is_drawed = True
        return ''.join(self.log)

    def open_log_window(self, pr, language):
        """ Окно с логом"""
        pr.init_window(750, 850, "Port Scanner Log")
        pr.set_target_fps(30)
        pr.set_window_icon(pr.load_image('portscanner.png'))
        logging.info("Log window initialized")
        while not pr.window_should_close():
            pr.begin_drawing()
            pr.clear_background(colors.WHITE)
            pr.draw_rectangle_gradient_ex(pr.Rectangle(0, 0, 750, 850), \
                                colors.DARKGRAY, colors.DARKGRAY, colors.BLACK, colors.BLACK)
            pr.draw_line(25,50,725,50,colors.WHITE)
            pr.draw_text_ex(language.font, "Log:", \
                            pr.Vector2(5, 5), 25, 1, colors.WHITE)

            pr.draw_text_ex(language.font, self.get_log(), \
                            pr.Vector2(5, 75), 12, 1, colors.WHITE)

            pr.end_drawing()
        pr.close_window()
