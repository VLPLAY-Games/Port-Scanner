""" Файл для работы с языком"""
import logging
from os.path import exists
from translators import RUSSIAN_LANGUAGE, TRANSLATES_RU

class Language:
    """ Класс для работы с языком"""
    def __init__(self):
        """ Инициализация """
        logging.info("Started Language class initializing")
        self.font = []
        self.lang_file = __file__
        self.selected_lang = ""
        self.translates_ru = TRANSLATES_RU
        logging.info("Loaded translates to Russian language")
        self.temp = ""
        logging.info("Language class initialized successfully")

    def __del__(self):
        """ Деинициализация """
        logging.info("Language class deinitialized")

    def change_language(self, pr, lang_name):
        """ Функция смены языка"""
        try:
            self.lang_file = open("lang.cfg", "w", encoding="utf-8")
            if lang_name == "RU":
                self.selected_lang = "RU"
                self.lang_file.write("RU")
                pr.unload_font(self.font)
                self.font = pr.load_font_ex('fonts/cyrillic.ttf', 50, None, 0)
                logging.info("Changed language to Russian")
            elif lang_name == "EN":
                self.selected_lang = "EN"
                self.lang_file.write("EN")
                pr.unload_font(self.font)
                self.font = pr.load_font_ex('fonts/english.ttf', 50, None, 0)
                logging.info("Changed language to English")
            self.lang_file.close()
        except Exception as e:
            self.lang_file.close()
            logging.error("Error while changing language " + str(e))

    def get_text_tr(self, text):
        """ Получение текста по языку"""
        self.temp = ""
        if self.selected_lang == "EN":
            return text
        elif self.selected_lang == "RU":
            for letter in self.translates_ru[text]:
                self.temp += chr(RUSSIAN_LANGUAGE[letter])
            return self.temp

    def set_lang_startup(self, pr):
        """ Изменение языка при запуске программы"""
        if (exists('lang.cfg') is False):
            logging.warning("Language file doesn't exist")
            self.lang_file = open("lang.cfg", "w")
            self.lang_file.write("EN")
            self.lang_file.close()
            logging.info("Created language file successfuly")
        self.lang_file = open("lang.cfg", "r")
        try:
            self.selected_lang = self.lang_file.readline()
            self.lang_file.close()
            if (self.selected_lang == "EN"):
                self.font = pr.load_font_ex('fonts/english.ttf', 50, None, 0)
            elif (self.selected_lang == "RU"):
                self.font = pr.load_font_ex('fonts/cyrillic.ttf', 50, None, 0)
            logging.info("Set language " + self.selected_lang + " sucessfully")

        except Exception as e:
            logging.error("Error while reading language file " + str(e))
            logging.info("Set default language")
            self.font = pr.load_font_ex('fonts/english.ttf', 50, None, 0)
            self.selected_lang = "EN"
            self.lang_file = open("lang.cfg", "w", encoding="utf-8")
            self.lang_file.write("EN")
            self.lang_file.close()


class Language_English():
    def __init__(self, pr):
        self.font = pr.load_font_ex('fonts/english.ttf', 50, None, 0)

    def __del__(self):
        """ Деинициализация """
        pass