""" Файл для работы с приложением"""

import logging
from config import WIDTH, HEIGHT, FPS, APP_NAME, VERSION

class App():
    """ Основной класс приложения"""
    def __init__(self):
        """ Инициализация класса """
        self.version = VERSION
        self.width = WIDTH
        self.height = HEIGHT
        self.fps = FPS
        self.app_name = APP_NAME
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
            pr.set_window_icon(pr.load_image("images/portscanner.png"))
            logging.info("App initialized")
        except Exception as e:
            logging.critical("Error while initializing App window: " + str(e))

    def draw_main(self, pr, colors, terminal, task, language):
        """ Отрисовка дизайна приложения """
        pr.draw_rectangle_gradient_ex(pr.Rectangle(0, 0, self.width, self.height), \
                                      colors.DARKGRAY, colors.DARKGRAY, colors.BLACK, colors.BLACK)
        pr.draw_line(500,25,500,575,colors.WHITE)
        pr.draw_line(25,575,975,575,colors.WHITE)
        pr.draw_line(25,25,975,25,colors.WHITE)
        pr.draw_text_ex(language.font, language.get_text_tr("Select_option"), \
                        pr.Vector2(50,50), 25, 1,colors.WHITE)
        pr.draw_text_ex(language.font, "Enter IP and ports", \
                        pr.Vector2(50, 175), 15, 1, colors.WHITE)
        terminal.draw_terminal(pr, colors, task, language)
        pr.draw_text_ex(language.font, APP_NAME + " by VL_PLAY Games " + self.version,\
                         pr.Vector2(725, 585), 12, 1, colors.WHITE)

    def error_init(self, e, pr, colors, language, log):
        """ Отрисовка ошибки """
        logging.critical(str(e) + self.version)
        pr.close_window()
        pr.init_window(300, 300, "Port Scanner Critical Error")
        pr.set_target_fps(30)
        pr.set_window_icon(pr.load_image('images/portscanner.png'))
        language.set_lang_startup(pr)
        logging.info("Error window initialized")
        while not pr.window_should_close():
            pr.begin_drawing()
            pr.clear_background(colors.WHITE)
            pr.draw_rectangle_gradient_ex(pr.Rectangle(0, 0, 300, 300), \
                            colors.DARKGRAY, colors.DARKGRAY, colors.BLACK, colors.BLACK)
            pr.draw_text_ex(language.font, "Critical Error", \
                            pr.Vector2(75, 75), 25, 1, colors.WHITE)
            pr.draw_text_ex(language.font, "Check report.log", \
                            pr.Vector2(90, 125), 15, 1, colors.WHITE)
            if pr.gui_button(
                    pr.Rectangle(125, 175, 50, 25),
                    'Log'):
                pr.close_window()
                log.open_log_window(pr, language)
            pr.draw_rectangle_gradient_ex(pr.Rectangle(125, 175, 50, 25), \
                            colors.DARKGREEN, colors.DARKGREEN, colors.DARKBLUE, colors.DARKBLUE)
            pr.draw_text_ex(language.font, 'Log', pr.Vector2(135,185), 11, 1, colors.WHITE)
            pr.end_drawing()
        pr.close_window()

    def exception(self, text, e, terminal, task):
        """ Обработка исключений """
        logging.error(text)
        logging.error(str(e))
        terminal.terminal_active = False
        task.task = ""
        self.enter_pressed = False
        terminal.draw_text += "An error has occurred"

    def fast_draw_text(self, text, pr, colors, terminal, task, language):
        """ Отрисовать перед выполнением задачи текст"""
        self.draw_main(pr, colors, terminal, task, language)
        pr.begin_drawing()
        pr.draw_text_ex(language.font, text, pr.Vector2(550, 125), 12, 1, colors.WHITE)
        pr.clear_background(colors.WHITE)
        pr.end_drawing()
        pr.begin_drawing()
