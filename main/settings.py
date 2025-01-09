""" Файл для работы с настройками приложения """

import logging
from os.path import exists
import config
import colors

class Settings:
    """ Класс для работы с клавиатурой"""
    def __init__(self, pr):
        """ Инициализация """
        logging.info("Started Settings class initializing")
        self.initialize_defaults()

        try:
            self.app_cfg = open('app.cfg', 'r', encoding="utf-8")
            self.main_func()
        except Exception as e:
            logging.critical("Error while initializing Settings class: %s", str(e))
            logging.critical("Trying to check App config")
            self.check_app_config(True)
            self.app_cfg = open('app.cfg', 'r', encoding="utf-8")
            self.main_func()

        self.log_settings(pr)
        logging.info("Settings class initialized successfully")

    def initialize_defaults(self):
        """Инициализация настроек по умолчанию"""
        self.app_cfg = None
        self.width = self.height = self.fps = self.font_size = 0
        self.but_width = self.but_height = self.but_font_size = 0
        self.language = ""
        self.log_level = 0

        self.font_size_small = config.FONT_SIZE_SMALL
        self.font_size_middle = config.FONT_SIZE
        self.font_size_big = config.FONT_SIZE_BIG

        self.but_font_size_small = config.BUT_FONT_SIZE_SMALL
        self.but_font_size_middle = config.BUT_FONT_SIZE
        self.but_font_size_big = config.BUT_FONT_SIZE_BIG

        self.but_width_small = config.BUT_WIDTH_SMALL
        self.but_height_small = config.BUT_HEIGHT_SMALL
        self.but_width_middle = config.BUT_WIDTH
        self.but_height_middle = config.BUT_HEIGHT
        self.but_width_big = config.BUT_WIDTH_BIG
        self.but_height_big = config.BUT_HEIGHT_BIG

        self.about = config.ABOUT
        self.app_name = config.APP_NAME
        self.version = config.VERSION
        self.info = config.INFORMATION

    def log_settings(self, pr):
        """Логирование установленных настроек"""
        logging.info("Set app width to %s", self.width)
        logging.info("Set app height to %s", self.height)
        logging.info("Set app FPS to %s", self.fps)
        logging.info("Set app font size to %s", self.font_size)
        logging.info("Set app buttons default width to %s", self.but_width)
        logging.info("Set app buttons default height to %s", self.but_height)
        logging.info("Set app buttons default font size to %s", self.but_font_size)
        logging.info("Set app name to %s", self.app_name)
        logging.info("Set app version to %s", self.version)
        pr.set_trace_log_level(self.log_level)
        logging.info("Set app log level to %s", self.log_level)
        logging.info("Loaded information")

    def __del__(self):
        """ Деинициализация """
        if self.app_cfg and not self.app_cfg.closed:
            self.app_cfg.close()
            logging.info("App configuration file closed")
        logging.info("Settings class deinitialized")

    def main_func(self):
        """ Основная функция при инциализации класса """
        self.temp = [line.strip().split('=')[1] for line in self.app_cfg]
        self.app_cfg.close()

        (self.width, self.height, self.fps, self.font_size,
         self.but_width, self.but_height, self.but_font_size,
         self.language, self.log_level) = map(self._convert_config_value, self.temp)

    @staticmethod
    def _convert_config_value(value):
        """Преобразует значение конфигурации в нужный тип"""
        try:
            return int(value)
        except ValueError:
            return value

    def settings_window(self, pr, language, button):
        """ Запуск приложения """
        try:
            pr.init_window(self.width, self.height, self.app_name + " Settings")
            pr.set_target_fps(self.fps)
            pr.set_window_icon(pr.load_image("images/portscanner.png"))
            language.set_lang_startup(pr)
            logging.info("Settings window initialized")
        except Exception as e:
            logging.critical("Error while initializing Settings window: %s", str(e))

        while not pr.window_should_close():
            pr.begin_drawing()
            pr.clear_background(colors.WHITE)
            pr.draw_rectangle_gradient_ex(pr.Rectangle(0, 0, self.width, self.height), \
                                        colors.DARKGRAY, colors.DARKGRAY, \
                                        colors.BLACK, colors.BLACK)
            pr.draw_text_ex(language.font, language.get_text_tr("Settings"), \
                            pr.Vector2(50,25), 30, 1,colors.WHITE)
            pr.draw_text_ex(language.font, language.get_text_tr("Font size"), \
                            pr.Vector2(100,100), 25, 1,colors.WHITE)
            pr.draw_text_ex(language.font, language.get_text_tr("Button font size"), \
                            pr.Vector2(75,325), 25, 1,colors.WHITE)
            pr.draw_text_ex(language.font, language.get_text_tr("Log level"), \
                            pr.Vector2(425, 100), 25, 1,colors.WHITE)
            pr.draw_text_ex(language.font, language.get_text_tr("Button size"), \
                            pr.Vector2(425,325), 25, 1,colors.WHITE)
            pr.draw_line(25,525,975,525,colors.WHITE)
            pr.draw_line(25,75,975,75,colors.WHITE)
            pr.draw_line(325,75,325,self.height-75,colors.WHITE)
            pr.draw_line(650,75,650,self.height-75,colors.WHITE)
            pr.draw_line(25, int(self.height / 2), \
                         self.width - 25, int(self.height / 2), colors.WHITE)
            button.check_buttons_settings(pr, language, self)
            pr.end_drawing()

        pr.close_window()

    def write_settings(self, name, value):
        """ Изменение параметров в файле конфига"""
        try:
            updated = False
            # Читаем и обновляем строки конфигурации
            with open('app.cfg', 'r', encoding='utf-8') as f:
                lines = f.readlines()

            with open('app.cfg', 'w', encoding='utf-8') as f:
                for line in lines:
                    key, *rest = line.strip().split('=', 1)
                    if key == name:
                        f.write(f"{name}={value}\n")
                        updated = True
                    else:
                        f.write(line)

                # Добавляем новый параметр, если он отсутствует
                if not updated:
                    f.write(f"{name}={value}\n")

            # Динамически обновляем атрибут объекта, если он существует
            attr_map = {
                "font_size": "font_size",
                "button_width": "but_width",
                "button_height": "but_height",
                "button_font_size": "but_font_size",
                "loglevel": "log_level"
            }
            if name in attr_map:
                setattr(self, attr_map[name], value)

            logging.info("Changed in app config %s to %s", name, str(value))

        except Exception as e:
            logging.error("Error while changing app config: %s", str(e))


    def create_app_config(self, recreate=False):
        """ Создание конфигурационного файла приложения"""
        try:
            if not exists("app.cfg") or recreate:
                message = "App config file doesn't exist" \
                    if not recreate else "App config file needs to be recreated"
                logging.warning(message)

                config_values = {
                    "width": config.WIDTH,
                    "height": config.HEIGHT,
                    "fps": config.FPS,
                    "font_size": config.FONT_SIZE,
                    "button_width": config.BUT_WIDTH,
                    "button_height": config.BUT_HEIGHT,
                    "button_font_size": config.BUT_FONT_SIZE,
                    "language": config.LANGUAGE,
                    "loglevel": config.LOG_LEVEL
                }

                with open('app.cfg', 'w', encoding='utf-8') as app_cfg:
                    app_cfg.writelines(f"{key}={value}\n" for key, value in config_values.items())

                logging.info("Created app.cfg with default values")
        except Exception as e:
            logging.error("Error while creating app config: %s", str(e))

    def check_app_config(self, recreate=False):
        """ Проверка конфигурационного файла """

        logging.info("Checking app config file")

        # Ожидаемые параметры, их условия проверки и значения по умолчанию
        expected_config = {
            "width": (lambda x: x.isdigit() and int(x) > 0, "1000"),
            "height": (lambda x: x.isdigit() and int(x) > 0, "600"),
            "fps": (lambda x: x.isdigit() and int(x) > 0, "30"),
            "font_size": (lambda x: x.isdigit() and int(x) > 0, "18"),
            "button_width": (lambda x: x.isdigit() and int(x) > 0, "100"),
            "button_height": (lambda x: x.isdigit() and int(x) > 0, "55"),
            "button_font_size": (lambda x: x.isdigit() and int(x) > 0, "18"),
            "language": (lambda x: x in ["EN", "RU"], "EN"),
            "loglevel": (lambda x: x.isdigit() and 0 <= int(x) <= 7, "3"),
        }

        def validate_and_correct_config(config_lines):
            config_dict = {}
            for line in config_lines:
                if "=" in line:
                    key, value = line.split("=", 1)
                    config_dict[key.strip()] = value.strip()

            corrected = False
            # Проверяем наличие всех ключей и их значения
            for key, (validator, default) in expected_config.items():
                if key not in config_dict or not validator(config_dict[key]):
                    config_dict[key] = default
                    corrected = True

            return config_dict, corrected

        try:
            with open('app.cfg', 'r', encoding="utf-8") as cfg_file:
                config_lines = [line.strip() for line in cfg_file if line.strip()]

            config_dict, corrected = validate_and_correct_config(config_lines)

            if corrected or recreate:
                logging.warning("App config file corrected or recreated.")
                with open('app.cfg', 'w', encoding="utf-8") as cfg_file:
                    for key, value in config_dict.items():
                        cfg_file.write(f"{key}={value}\n")
            else:
                logging.info("App config file is valid")

        except FileNotFoundError:
            logging.error("App config file not found, recreating")
            self.create_app_config(True)
        except Exception as e:
            logging.error("Unexpected error: %s, recreating config", str(e))
            self.create_app_config(True)

    def get_button_gradient_width(self):
        """ Получение ширины для красивого фона кнопок"""
        gradient_offsets = {
            config.BUT_WIDTH: 12,
            config.BUT_WIDTH_SMALL: 10,
            config.BUT_WIDTH_BIG: 15
        }
        return self.but_width + gradient_offsets.get(self.but_width, 0)


    def get_button_gradient_height(self):
        """ Получение высоты для красивого фона кнопок"""
        gradient_offsets = {
            config.BUT_HEIGHT: 7,
            config.BUT_HEIGHT_SMALL: 6,
            config.BUT_HEIGHT_BIG: 9
        }
        return self.but_height + gradient_offsets.get(self.but_height, 0)


    def get_button_color(self, but_name):
        """ Получение цвета кнопок в настройках выбрано или нет"""
        font_sizes = {
            "fs_s": config.FONT_SIZE_SMALL,
            "fs_m": config.FONT_SIZE,
            "fs_b": config.FONT_SIZE_BIG,
        }

        but_font_sizes = {
            "bfs_s": config.BUT_FONT_SIZE_SMALL,
            "bfs_m": config.BUT_FONT_SIZE,
            "bfs_b": config.BUT_FONT_SIZE_BIG,
        }

        button_sizes = {
            "bs_s": (config.BUT_WIDTH_SMALL, config.BUT_HEIGHT_SMALL),
            "bs_m": (config.BUT_WIDTH, config.BUT_HEIGHT),
            "bs_b": (config.BUT_WIDTH_BIG, config.BUT_HEIGHT_BIG),
        }

        log_levels = {
            "log_0": 7,
            "log_1": 0,
            "log_2": 2,
            "log_3": 3,
            "log_4": 4,
            "log_5": 5,
            "log_6": 6,
        }

        if but_name in font_sizes:
            return colors.DARKGREEN if self.font_size == font_sizes[but_name] else colors.DARKBLUE

        if but_name in but_font_sizes:
            return colors.DARKGREEN if self.but_font_size == but_font_sizes[but_name] \
                else colors.DARKBLUE

        if but_name in button_sizes:
            width, height = button_sizes[but_name]
            return colors.DARKGREEN if (self.but_width == width and self.but_height == height) \
                else colors.DARKBLUE

        if but_name in log_levels:
            return colors.DARKGREEN if self.log_level == log_levels[but_name] else colors.DARKBLUE

        return colors.DARKBLUE


    def exit(self, pr):
        """ Закрытие окна настроек"""
        pr.close_window()
