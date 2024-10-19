""" Файл для работы с языком"""
import logging
class Language:
    def __init__(self):
        """ Инициализация """
        logging.info("Language class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("Language class deinitialized")

    def change_language(self, pr, lang_name):
        """ Функция смены языка"""
        try:
            if lang_name == "RU":
                pass
                # pr.load_font_from_memory()
            elif lang_name == "EN":
                pass
                # pr.load_font_from_memory()
        except Exception as e:
            logging.error("Error while changing language " + str(e))
