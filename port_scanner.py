""" Сканер портов """

# Библиотеки
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
from log import Log
from config import information

def log_to_file(log_type, message, _):
        with open("report.log", "a+") as log_file:
            log_file.write(f"{log_type}: {message}n")

def main():
    """ Основная функция """
    log = Log()
    app = App()
    ip = Ip()
    task = Task()
    port = Port()
    keyboard = Keyboard()
    button = Button()
    terminal = Terminal()
    language = Language(pr)
    pr.set_trace_log_level(4)
    try:
        app.init_app(pr)
        while not pr.window_should_close():
            pr.begin_drawing()
            app.draw_main(pr, colors, terminal, task, language)
            button.check_all_but(ip, pr, terminal, task, app, language, information, log)
            keyboard.check_key(pr, terminal)
            task.check_task(app, ip, port, keyboard, pr, colors, terminal, task, language)
            terminal.draw_terminal_text(keyboard.get_keys(), pr, colors, language)
            pr.clear_background(colors.WHITE)
            pr.end_drawing()

        pr.close_window()
    except Exception as e:
        app.error_init(e, pr, colors, language, log)
    del app, ip, task, port, keyboard, button, terminal, language, log
    logging.info("App is closed")

if __name__ == '__main__':
    main()
