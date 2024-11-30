""" Файл для работы с настройками приложения """

import logging
import config
import colors
from os.path import exists

class Settings:
    """ Класс для работы с клавиатурой"""
    def __init__(self):
        """ Инициализация """
        logging.info("Started Settings class initializing")
        self.app_cfg = __file__
        self.width = config.WIDTH
        logging.info("Set app width to " + str(self.width))
        self.height = config.HEIGHT
        logging.info("Set app height to " + str(self.height))
        self.fps = config.FPS
        logging.info("Set app FPS to " + str(self.fps))
        self.app_name = config.APP_NAME
        logging.info("Set app name to " + str(self.app_name))
        self.version = config.VERSION
        logging.info("Set app version to " + str(self.version))
        self.info = config.INFORMATION
        logging.info("Loaded information")
        self.font_size = config.FONT_SIZE
        logging.info("Set app font size to " + str(self.font_size))
        self.but_width = config.BUT_WIDTH
        logging.info("Set app buttons default width to " + str(self.but_width))
        self.but_height = config.BUT_HEIGHT
        logging.info("Set app buttons default height to " + str(self.but_height))
        self.but_font_size = config.BUT_FONT_SIZE
        logging.info("Set app buttons default font size to " + str(self.but_font_size))
        self.app_config()
        logging.info("Settings class initialized successfully")

    def __del__(self):
        """ Деинициализация """
        logging.info("Settings class deinitialized")


    def settings_window(self, pr):
        """ Запуск приложения """
        try:
            pr.init_window(self.width, self.height, self.app_name)
            pr.set_target_fps(self.fps)
            pr.set_window_icon(pr.load_image("images/portscanner.png"))
            logging.info("Settings window initialized")
        except Exception as e:
            logging.critical("Error while initializing Settings window: " + str(e))

        while not pr.window_should_close():
            pr.begin_drawing()
            pr.clear_background(colors.WHITE)
            pr.end_drawing()

        pr.close_window()

    def app_config(self):
        logging.info("Checking app config")
        if (exists('app.cfg') is False):
            logging.warning("app.cfg file doesn't exists")
            self.app_cfg = open("app.cfg", 'a')
            self.app_cfg.write(str(self.width) + "\n")
            self.app_cfg.write(str(self.height) + "\n")
            self.app_cfg.write(str(self.fps) + "\n")
            self.app_cfg.write(str(self.but_font_size) + "\n")
            self.app_cfg.write(str(self.but_width) + "\n")
            self.app_cfg.write(str(self.but_height) + "\n")
            self.app_cfg.close()
            logging.info("app.cfg file initialized with default parametres")
        logging.info("Checked app config")