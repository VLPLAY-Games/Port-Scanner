""" Файл для работы с языком """
import logging
from translators import RUSSIAN_LANGUAGE, TRANSLATES_RU


class Language:
    """ Класс для работы с языком """
    def __init__(self, settings):
        """ Инициализация """
        logging.info("Started Language class initializing")
        self.font = []
        self.lang_file = __file__
        self.selected_lang = settings.language
        self.translates_ru = TRANSLATES_RU
        logging.info("Loaded translates to Russian language")
        self.temp = ""
        logging.info("Language class initialized successfully")

    def __del__(self):
        """ Деинициализация """
        logging.info("Language class deinitialized")

    def change_language(self, pr, lang_name, settings):
        """ Функция смены языка """
        try:
            if lang_name == "RU":
                settings.write_settings("language", lang_name)
                self.selected_lang = "RU"
                pr.unload_font(self.font)
                self.font = pr.load_font_ex('fonts/cyrillic.ttf', 50, None, 0)
                logging.info("Changed language to Russian")
            elif lang_name == "EN":
                settings.write_settings("language", lang_name)
                self.selected_lang = "EN"
                pr.unload_font(self.font)
                self.font = pr.load_font_ex('fonts/english.ttf', 50, None, 0)
                logging.info("Changed language to English")
        except (FileNotFoundError, ValueError) as e:
            logging.error("Error while changing language: %s", str(e))

    def get_text_tr(self, text):
        """ Получение текста по языку """
        if self.selected_lang == "EN":
            return text
        if self.selected_lang == "RU":
            self.temp = "".join(chr(RUSSIAN_LANGUAGE[letter]) \
                                for letter in self.translates_ru[text])
            return self.temp
        return None

    def set_lang_startup(self, pr):
        """ Изменение языка при запуске программы """
        try:
            if self.selected_lang == "EN":
                self.font = pr.load_font_ex('fonts/english.ttf', 50, None, 0)
            elif self.selected_lang == "RU":
                self.font = pr.load_font_ex('fonts/cyrillic.ttf', 50, None, 0)
            logging.info("Set language %s successfully", self.selected_lang)
        except FileNotFoundError as e:
            logging.error("Error while reading language file: %s", str(e))
            logging.info("Set default language")
            self.font = pr.load_font_ex('fonts/english.ttf', 50, None, 0)


class LanguageEnglish:
    """ Класс для английского языка терминала и лога """
    def __init__(self):
        self.font = []

    def set_english(self, pr):
        """ Установка английского языка """
        self.font = pr.load_font_ex('fonts/english.ttf', 50, None, 0)

    def __del__(self):
        """ Деинициализация """
        pass
