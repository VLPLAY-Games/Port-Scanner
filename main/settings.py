""" Файл для работы с настройками приложения """

import logging
import config

class Settings:
    """ Класс для работы с клавиатурой"""
    def __init__(self):
        """ Инициализация """
        logging.info("Started Settings class initializing")
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
        logging.info("Settings class initialized successfully")

    def __del__(self):
        """ Деинициализация """
        logging.info("Settings class deinitialized")
