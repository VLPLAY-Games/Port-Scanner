""" Файл для работы с языком"""
import logging
from os.path import exists

class Language:
    """ Класс для работы с языком"""
    def __init__(self, pr):
        """ Инициализация """
        self.font = []
        if (exists("lang.cfg") == False):
            self.lang_file = open("lang.cfg", "w")
            self.lang_file.write("EN")
            self.lang_file.close()
        self.lang_file = open("lang.cfg", "r")
        try:
            self.selected_lang = self.lang_file.readline()
            self.lang_file.close()
            if (self.selected_lang == "EN"):
                self.font = pr.load_font_ex('fonts/english.ttf', 50, None, 0)
            elif (self.selected_lang == "RU"):
                self.font = pr.load_font_ex('fonts/cyrillic.ttf', 50, None, 0) 
          

        except Exception as e:
            logging.warning("Error while reading language file " + str(e))
            self.font = pr.load_font_ex('fonts/english.ttf', 50, None, 0)
            self.selected_lang = "EN"
            self.lang_file = open("lang.cfg", "w")
            self.lang_file.write("EN")
            self.lang_file.close()


        self.translates_ru = {
            "Select_option" : "Выберите опцию",
            "Check_your_ip" : "Проверить IP",
            "Check_all_ports" : "Проверить все порты",
            "All_info" : "Вся информация",
            "Start": "Старт",
            "Help" : "Помощь",
            "Log" : "Логи",
            "Result" : "Результаты",
        }

        self.translates_en = {
            "Select_option" : "Select option",
            "Check_your_ip" : "Check your IP",
            "Check_all_ports" : "Check all ports",
            "All_info" : "All info",
            "Start": "Start",
            "Help" : "Help",
            "Log" : "Log",
            "Result" : "Result",
        }
        logging.info("Language class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("Language class deinitialized")

    def change_language(self, pr, lang_name):
        """ Функция смены языка"""
        try:
            self.lang_file = open("lang.cfg", "w")
            if lang_name == "RU":
                self.selected_lang = "RU"
                self.lang_file.write("RU")
                self.font = pr.load_font_ex('fonts/cyrillic.ttf', 50, None, 0)
                logging.info("Changed language to Russian")
            elif lang_name == "EN":
                self.selected_lang = "EN"
                self.lang_file.write("EN")
                self.font = pr.load_font_ex('fonts/english.ttf', 50, None, 0)
                logging.info("Changed language to English")
                self.lang_file.close()
        except Exception as e:
            self.lang_file.close()
            logging.error("Error while changing language " + str(e))

    def get_text_tr(self, text):
        if self.selected_lang == "EN":
            return self.translates_en[text]
        elif self.selected_lang == "RU":
            return self.translates_ru[text]
        