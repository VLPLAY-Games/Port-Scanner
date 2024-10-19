""" Сканер портов """

# Библиотеки
import os
import logging
import pyray as pr
from raylib import colors
from app import App
from ip import Ip
from port import Port
from keyboard import Keyboard
from task import Task
from button import Button
from terminal import Terminal
from language import Language

def main():
    """ Основная функция """
    os.remove("report.log")
    # Логирование приложения
    logging.basicConfig(filename='report.log', format='%(asctime)s - %(levelname)s - %(message)s', \
                level=logging.INFO)
    logging.info("             Port scanner                 ")
    logging.info("App started")
    app = App()
    ip = Ip()
    task = Task()
    port = Port()
    keyboard = Keyboard()
    button = Button()
    terminal = Terminal()
    language = Language()
    try:
        app.init_app(pr)
        while not pr.window_should_close():
            pr.begin_drawing()
            app.draw_main(pr, colors, terminal, task)
            button.check_all_but(ip, pr, terminal, task, app, language)
            keyboard.check_key(pr, terminal)
            task.check_task(app, ip, port, keyboard, pr, colors, terminal, task)
            terminal.draw_terminal_text(keyboard.get_keys(), pr, colors)
            pr.clear_background(colors.WHITE)
            pr.end_drawing()

        pr.close_window()
    except Exception as e:
        app.error_init(e, pr, colors)
    del app, ip, task, port, keyboard, button, terminal, language
    logging.info("App is closed")

if __name__ == '__main__':
    main()
