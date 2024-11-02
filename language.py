""" Файл для работы с языком"""
import logging

class Language:
    """ Класс для работы с языком"""
    def __init__(self, pr):
        """ Инициализация """
        self.font = pr.load_font_ex('fonts/english.ttf', 40, None, 0)
        self.selected_lang = "EN"
        logging.info("Language class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("Language class deinitialized")

    def change_language(self, pr, lang_name):
        """ Функция смены языка"""
        try:
            if lang_name == "RU":
                self.selected_lang = "RU"
                self.font = pr.load_font_ex('fonts/cyrillic.ttf', 35, None, 0)
            elif lang_name == "EN":
                self.selected_lang = "EN"
                self.font = pr.load_font_ex('fonts/english.ttf', 35, None, 0)
        except Exception as e:
            logging.error("Error while changing language " + str(e))
