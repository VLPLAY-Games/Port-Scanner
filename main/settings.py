""" Файл для работы с настройками приложения """

import logging
from os.path import exists
import config
import colors

class Settings:
    """ Класс для работы с клавиатурой"""
    def __init__(self, pr):
        """ Инициализация """
        logging.info("Started Settings class initializing")
        self.app_cfg = __file__
        self.check_app_config()
        self.width, self.height, self.fps, self.font_size, \
            self.but_width, self.but_height, self.but_font_size, self.language, self.log_level = \
                0, 0, 0, 0, 0, 0, 0, "", 0
        self.font_size_small = config.FONT_SIZE_SMALL
        self.font_size_middle = config.FONT_SIZE
        self.font_size_big = config.FONT_SIZE_BIG
        self.but_font_size_small = config.BUT_FONT_SIZE_SMALL
        self.but_font_size_middle = config.BUT_FONT_SIZE
        self.but_font_size_big = config.BUT_FONT_SIZE_BIG
        self.but_width_small = config.BUT_WIDTH_SMALL
        self.but_height_small = config.BUT_HEIGHT_SMALL
        self.but_width_middle = config.BUT_WIDTH
        self.but_height_middle = config.BUT_HEIGHT
        self.but_width_big = config.BUT_WIDTH_BIG
        self.but_height_big = config.BUT_HEIGHT_BIG
        self.app_cfg = open('app.cfg','r', encoding="utf-8")
        try:
            self.main_func()
        except Exception as e:
            logging.critical("Error while initializing Settings class: " + str(e))
            logging.critical("Trying to check App config")
            self.check_app_config(True)
            self.app_cfg = open('app.cfg','r', encoding="utf-8")
            self.main_func()

        logging.info("Set app width to " + str(self.width))
        logging.info("Set app height to " + str(self.height))
        logging.info("Set app FPS to " + str(self.fps))
        self.app_name = config.APP_NAME
        logging.info("Set app name to " + str(self.app_name))
        self.version = config.VERSION
        logging.info("Set app version to " + str(self.version))
        logging.info("Set app font size to " + str(self.font_size))
        logging.info("Set app buttons default width to " + str(self.but_width))
        logging.info("Set app buttons default height to " + str(self.but_height))
        logging.info("Set app buttons default font size to " + str(self.but_font_size))
        pr.set_trace_log_level(self.log_level)
        logging.info("Set app log level to " + str(self.log_level))

        self.info = config.INFORMATION
        logging.info("Loaded information")

        logging.info("Settings class initialized successfully")

    def __del__(self):
        """ Деинициализация """
        logging.info("Settings class deinitialized")

    def main_func(self):
        """ Основная функция при инциализации класса """
        self.temp = []
        for line in self.app_cfg.readlines():
            self.temp.append(line.strip().split(sep='=')[1])
        self.app_cfg.close()
        self.width, self.height, self.fps, self.font_size, \
            self.but_width, self.but_height, self.but_font_size, self.language, self.log_level = \
            self.temp
        self.width = int(self.width)
        self.height = int(self.height)
        self.fps = int(self.fps)
        self.font_size = int(self.font_size)
        self.but_width = int(self.but_width)
        self.but_height = int(self.but_height)
        self.but_font_size = int(self.but_font_size)
        self.log_level = int(self.log_level)

    def settings_window(self, ip, pr, terminal, task, app, language, log, settings, button):
        """ Запуск приложения """
        try:
            pr.init_window(self.width, self.height, self.app_name + " Settings")
            pr.set_target_fps(self.fps)
            pr.set_window_icon(pr.load_image("images/portscanner.png"))
            language.set_lang_startup(pr)
            logging.info("Settings window initialized")
        except Exception as e:
            logging.critical("Error while initializing Settings window: " + str(e))

        while not pr.window_should_close():
            pr.begin_drawing()
            pr.clear_background(colors.WHITE)
            pr.draw_rectangle_gradient_ex(pr.Rectangle(0, 0, self.width, self.height), \
                                        colors.DARKGRAY, colors.DARKGRAY, \
                                        colors.BLACK, colors.BLACK)
            pr.draw_text_ex(language.font, language.get_text_tr("Settings"), \
                            pr.Vector2(50,25), 30, 1,colors.WHITE)
            pr.draw_text_ex(language.font, language.get_text_tr("Font size"), \
                            pr.Vector2(100,100), 25, 1,colors.WHITE)
            pr.draw_text_ex(language.font, language.get_text_tr("Button font size"), \
                            pr.Vector2(75,325), 25, 1,colors.WHITE)
            pr.draw_text_ex(language.font, language.get_text_tr("Log level"), \
                            pr.Vector2(425, 100), 25, 1,colors.WHITE)
            pr.draw_text_ex(language.font, language.get_text_tr("Button size"), \
                            pr.Vector2(425,325), 25, 1,colors.WHITE)
            pr.draw_line(25,525,975,525,colors.WHITE)
            pr.draw_line(25,75,975,75,colors.WHITE)
            pr.draw_line(325,75,325,self.height-75,colors.WHITE)
            pr.draw_line(650,75,650,self.height-75,colors.WHITE)
            pr.draw_line(25, int(self.height / 2),self.width - 25, int(self.height / 2),colors.WHITE)
            button.check_buttons_settings(ip, pr, terminal, task, app, language, log, self)
            pr.end_drawing()

        pr.close_window()

    def write_settings(self, name, value):
        """ Изменение параметров в файле конфига"""
        try:
            with open('app.cfg','r', encoding="utf-8") as f:
                lines = f.readlines()
            with open('app.cfg','w', encoding="utf-8") as f:
                for line in lines:
                    if line.strip("\n").split(sep='=')[0] != name:
                        f.write(line)
                    else:
                        f.write(name + "=" + str(value) + '\n')
            if name == "font_size":
                self.font_size = value
            elif name == "button_width":
                self.but_width = value
            elif name == "button_height":
                self.but_height = value
            elif name == "button_font_size":
                self.but_font_size = value
            logging.info("Changed in app config " + name + " to " + str(value))

        except Exception as e:
            logging.error("Error while changing app config " + str(e))
        

    def create_app_config(self, recreate = False):
        """ Создание конфигурационного файла приложения"""
        if (exists("app.cfg") is False) or recreate:
            logging.warning("App config file doesn't exists" if recreate is False\
                             else "App config file needs to be recreated")
            self.app_cfg = open('app.cfg','w', encoding="utf-8")
            self.app_cfg.write("width=" + str(config.WIDTH))
            self.app_cfg.write("\nheight=" + str(config.HEIGHT))
            self.app_cfg.write("\nfps=" + str(config.FPS))
            self.app_cfg.write("\nfont_size=" + str(config.FONT_SIZE))
            self.app_cfg.write("\nbutton_width=" + str(config.BUT_WIDTH))
            self.app_cfg.write("\nbutton_height=" + str(config.BUT_HEIGHT))
            self.app_cfg.write("\nbutton_font_size=" + str(config.BUT_FONT_SIZE))
            self.app_cfg.write("\nlanguage=" + str(config.LANGUAGE))
            self.app_cfg.write("\nloglevel=" + str(config.LOG_LEVEL))
            self.app_cfg.close()
            logging.info("Created app.cfg with default values")

    def check_app_config(self, recreate = False):
        """ Проверка конфигурационного файла """
        logging.info("Checking app config file")
        self.create_app_config()
        temp = []
        self.app_cfg = open('app.cfg', 'r', encoding="utf-8")
        for line in self.app_cfg.readlines():
            temp.append(line.strip())
        flag = True
        for item in temp:
            if len(item.split("=")) != 2:
                flag = False

        if flag is False or recreate:
            logging.error("App config file is corrupted")
            self.create_app_config(True)
            self.app_cfg = open('app.cfg','r', encoding="utf-8")
            self.main_func()

        logging.info("Checked App config file")

    def get_button_gradient_width(self):
        if self.but_width == config.BUT_WIDTH:
            return self.but_width + 12

        elif self.but_width == config.BUT_WIDTH_SMALL:
            return self.but_width + 10

        elif self.but_width == config.BUT_WIDTH_BIG:
            return self.but_width + 15
    
    def get_button_gradient_height(self):
        if self.but_height == config.BUT_HEIGHT:
            return self.but_height + 7

        elif self.but_height == config.BUT_HEIGHT_SMALL:
            return self.but_height + 6

        elif self.but_height == config.BUT_HEIGHT_BIG:
            return self.but_height + 9


    def exit(self, pr):
        pr.close_window()
