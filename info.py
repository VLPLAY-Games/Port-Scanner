import logging

class Information:
    """ Класс для работы с информацией"""
    def __init__(self):
        """ Инициализация """
        self.all_info_of_task = f""
        logging.info("Information class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("Information class deinitialized")