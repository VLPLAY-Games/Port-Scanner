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
from language import Language
from log import Log
from settings import Settings


def main():
    """ Основная функция """
    try:
        log = Log()
        settings = Settings(pr)
        app = App()
        ip = Ip()
        task = Task()
        port = Port()
        keyboard = Keyboard()
        button = Button()
        terminal = Terminal()
        language = Language(settings)
    except Exception as e:
        logging.critical("Error initializing components: %s", str(e))
        return

    try:
        pr.set_trace_log_callback(log.callback_signature)
    except Exception as e:
        logging.critical("Error setting trace log callback: %s", str(e))
        app.error_init(e, pr, colors, language, log, settings)

    try:
        app.init_app(pr, settings)
        language.set_lang_startup(pr)
        language.set_english(pr)
    except Exception as e:
        logging.critical("Error during app initialization or language setup: %s", str(e))
        app.error_init(e, pr, colors, language, log, settings)

    try:
        while not pr.window_should_close():
            try:
                pr.begin_drawing()
                try:
                    app.draw_main(pr, colors, terminal, task, language, settings)
                except Exception as e:
                    logging.critical("Critical error in app.draw_main: %s", str(e))
                    app.error_init(e, pr, colors, language, log, settings)

                try:
                    button.check_all_but(ip, pr, terminal, task, app, language, log, settings)
                except Exception as e:
                    logging.critical("Critical error in button checking: %s", str(e))
                    app.error_init(e, pr, colors, language, log, settings)

                try:
                    keyboard.check_key(pr, terminal)
                except Exception as e:
                    logging.critical("Critical error in keyboard checking: %s", str(e))
                    app.error_init(e, pr, colors, language, log, settings)

                try:
                    task.check_task(app, ip, port, keyboard, pr, \
                                    colors, terminal, task, language, settings)
                except Exception as e:
                    logging.critical("Critical error in task checking: %s", str(e))
                    app.error_init(e, pr, colors, language, log, settings)

                try:
                    terminal.draw_terminal_text(keyboard.get_keys(), pr, language)
                except Exception as e:
                    logging.critical("Critical error in drawing terminal text: %s", str(e))
                    app.error_init(e, pr, colors, language, log, settings)

                pr.clear_background(colors.WHITE)
                pr.end_drawing()

            except Exception as e:
                logging.critical("Error in drawing loop: %s", str(e))
                app.error_init(e, pr, colors, language, log, settings)

    except Exception as e:
        logging.critical("Error in main loop: %s", str(e))
        logging.warning("Trying to check App config")
        try:
            settings.check_app_config(True)
        except Exception as config_error:
            logging.critical("Error checking app config: %s", str(config_error))

        app.error_init(e, pr, colors, language, log, settings)
        pr.unload_font(language.english_font)

    finally:
        pr.unload_font(language.english_font)
        try:
            del app, ip, task, port, keyboard, button, terminal, language, settings, log
        except Exception as del_error:
            logging.error("Error during cleanup: %s", str(del_error))

        logging.info("App is closed")

if __name__ == '__main__':
    main()
