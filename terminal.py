import logging

class Terminal:
    """ Класс для работы с Терминалом """
    def __init__(self):
        """ Инициализация """
        self.page = 0
        self.draw_text = ""
        logging.info("Terminal class initialized")
    
    def __del__(self):
        """ Деинициализация """
        logging.info("Terminal class deinitialized")

    def draw_terminal(self, pr, colors):
        """ Отрисовка дизайна терминала """
        pr.draw_text("Result", 550,50,25,colors.BLACK)
        pr.draw_rectangle_lines(525, 100, 450, 450, colors.BLACK)
    
    def term_prev(self):
        """ Предыдущая страница """
        pass

    def term_next(self):
        """ Следующая страница """
        pass

    def draw_terminal_text(self, app, keys, pr, colors):
        """ Отрисовка терминала """
        pr.draw_text(self.draw_text + str(''.join(keys)) if app.terminal_active \
                    else self.draw_text, \
                    550, 125, 10, colors.BLACK)
