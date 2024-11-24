""" Файл для работы с настройками приложения """

import logging
import config

class Settings:
    """ Класс для работы с клавиатурой"""
    def __init__(self):
        """ Инициализация """
        logging.info("Started Settings class initializing")
        self.width = config.WIDTH
        self.height = config.HEIGHT
        self.fps = config.FPS
        self.app_name = config.APP_NAME
        self.version = config.VERSION
        self.info = config.INFORMATION
        self.font_size = config.FONT_SIZE
        self.but_width = config.BUT_WIDTH
        self.but_height = config.BUT_HEIGHT
        self.but_font_size = config.BUT_FONT_SIZE
        logging.info("Settings class initialized successfully")

    def __del__(self):
        """ Деинициализация """
        logging.info("Settings class deinitialized")
