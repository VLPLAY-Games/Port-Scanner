""" Сканер портов """

# Библиотеки
import logging
import pyray as pr
import colors
from app import App
from ip import Ip
from port import Port
from keyboard import Keyboard # type: ignore
from task import Task
from button import Button
from terminal import Terminal
from language import Language, Language_English
from log import Log
from settings import Settings

def main():
    """ Основная функция """
    
    log = Log()
    settings = Settings()
    app = App()
    ip = Ip()
    task = Task()
    port = Port()
    keyboard = Keyboard()
    button = Button()
    terminal = Terminal()
    language = Language()
    language_english = Language_English(pr)
    pr.set_trace_log_callback(log.callback_signature)
    # pr.set_trace_log_level(4)
    try:
        app.init_app(pr, settings)
        language.set_lang_startup(pr)
        while not pr.window_should_close():
            pr.begin_drawing()
            app.draw_main(pr, colors, terminal, task, language, settings)
            button.check_all_but(ip, pr, terminal, task, app, language, log, settings)
            keyboard.check_key(pr, terminal)
            task.check_task(app, ip, port, keyboard, pr, colors, terminal, task, language)
            terminal.draw_terminal_text(keyboard.get_keys(), pr, colors, language_english)
            pr.clear_background(colors.WHITE)
            pr.end_drawing()

        pr.close_window()
    except Exception as e:
        app.error_init(e, pr, colors, language_english, log, settings)
    pr.unload_font(language.font)
    pr.unload_font(language_english.font)
    del app, ip, task, port, keyboard, button, terminal, language, language_english, settings, log
    logging.info("App is closed")

if __name__ == '__main__':
    main()
