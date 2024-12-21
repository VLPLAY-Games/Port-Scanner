""" Файл для работы с логами"""
import logging
from os import remove
from datetime import datetime
import colors
from cffi import FFI

class Log:
    """ Класс для работы с логами"""
    def __init__(self):
        """ Инициализация """
        self.temp = 0
        self.log_lines = []
        self.log = []
        self.is_drawed = False
        self.temp = open("report.log", "a", encoding="utf-8")
        self.temp.close()
        self.arr_text = []
        self.page = 0
        self.draw_text = ""
        self.pages = 0

        self.LOG_ALL = 0       # All logs
        self.LOG_TRACE = 1     # Trace logging, intended for debugging
        self.LOG_DEBUG = 2     # Debug logging
        self.LOG_INFO = 3      # Info logging
        self.LOG_WARNING = 4   # Warning logging
        self.LOG_ERROR = 5     # Error logging
        self.LOG_FATAL = 6     # Fatal error logging
        self.LOG_NONE = 7      # Disable logging
        self.ffi = FFI()
        self.callback_signature = self.ffi.callback("void(int, const char *, void *)", \
                                                    self.custom_log)
        remove("report.log")
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
        if (self.is_drawed is False):
            self.log = []
            self.log_lines = []
            with open("report.log", encoding="utf-8") as file:
                self.log_lines = [line.rstrip() for line in file]
            for line in self.log_lines:
                self.log.append(line + '\n')
            if (terminal is False):
                self.is_drawed = True
        return ''.join(self.log)

    def open_log_window(self, pr, language, settings):
        """ Окно с логом"""
        pr.init_window(750, 850, "Port Scanner Log")
        pr.set_target_fps(settings.fps)
        pr.set_window_icon(pr.load_image('images/portscanner.png'))
        language.set_english(pr)
        logging.info("Log window initialized")
        while not pr.window_should_close():
            pr.begin_drawing()
            pr.clear_background(colors.WHITE)
            pr.draw_rectangle_gradient_ex(pr.Rectangle(0, 0, 750, 850), \
                                colors.DARKGRAY, colors.DARKGRAY, colors.BLACK, colors.BLACK)
            pr.draw_line(25,50,725,50,colors.WHITE)
            pr.draw_text_ex(language.font, "Log:", \
                            pr.Vector2(5, 5), 25, 1, colors.WHITE)

            self.but_next_console(pr, language)
            self.but_prev_console(pr, language)
            self.draw_terminal_text(pr, language)
            pr.end_drawing()
        pr.unload_font(language.font)
        pr.close_window()

    def custom_log(self, level, message, user_data):
        """ Кастомное логирование pyray"""
        now = datetime.now()
        time_str = (now.strftime("%Y-%m-%d %H:%M:%S") + f",{now.microsecond // 1000:03d}")

        log_prefix = {
            self.LOG_TRACE: "- TRACE - ",
            self.LOG_DEBUG: "- DEBUG - ",
            self.LOG_INFO: "- INFO - ",
            self.LOG_WARNING: "- WARN - ",
            self.LOG_ERROR: "- ERROR - ",
            self.LOG_FATAL: "- FATAL - ",
        }.get(level, "LOG  : ")

        formatted_message = f"{time_str} {log_prefix}{self.ffi.string(message).decode()}"
        with open("report.log", "a+", encoding="utf-8") as log_file:
            log_file.write(formatted_message + "\n")

    def check_pages(self):
        """ Проверка на несколько страниц"""
        self.arr_text = []
        temp_str = []

        for string in self.draw_text.split(sep="\n"):
            temp_str.append(string)

            if len(temp_str) >= 55:
                self.arr_text.append("\n".join(temp_str))
                temp_str = []

        if temp_str:
            self.arr_text.append("\n".join(temp_str))


    def term_prev(self):
        """ Предыдущая страница """
        if self.page > 0:
            self.page -= 1

    def term_next(self):
        """ Следующая страница """
        if self.page < self.pages - 1:
            self.page += 1

    def draw_terminal_text(self, pr, language):
        """ Отрисовка терминала """
        self.draw_text = self.get_log()
        self.check_pages()
        self.pages = len(self.arr_text)
        if len(self.arr_text) != 0:
            pr.draw_text_ex(language.font, str(self.arr_text[self.page]), \
                            pr.Vector2(5, 75), 12, 1, colors.WHITE)

    def but_next_console(self, pr, language):
        """ Отрисовка и обработка кнопки следующей страницы терминала """
        if pr.gui_button(
                    pr.Rectangle(700, 800, 40, 40), ""):
            self.term_next()
        pr.draw_rectangle_rounded(pr.Rectangle(698, 797, 46, 46), 0.5, 5, colors.AQUA)
        pr.draw_text_ex(language.font, '>>', pr.Vector2(710, 810), 25, 1, colors.WHITE)

    def but_prev_console(self, pr, language):
        """ Отрисовка и обработка кнопки предыдущей страницы терминала """
        if pr.gui_button(
                    pr.Rectangle(650, 800, 40, 40), ""):
            self.term_prev()
        pr.draw_rectangle_rounded(pr.Rectangle(648, 797, 46, 46), 0.5, 5, colors.AQUA)
        pr.draw_text_ex(language.font, '<<', pr.Vector2(660, 810), 25, 1, colors.WHITE)
