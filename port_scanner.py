""" Сканер портов """

# Библиотеки
import subprocess
import os
import socket
import logging
from concurrent.futures import ThreadPoolExecutor
import pyray as pr
import netifaces
from raylib import colors
from config import width, height, fps, app_name, version

class Terminal:
    """ Класс для работы с Терминалом """
    def __init__(self):
        """ Инициализация """
        self.page = 0
        logging.info("Terminal class initialized")
    
    def __del__(self):
        """ Деинициализация """
        logging.info("Terminal class deinitialized")

class Ip:
    """ Класс для работы с IP """
    def __init__(self):
        """ Инициализация """
        self.ipv4_list = []
        self.ipv6_list = []
        self.task_ip = ""
        logging.info("IP class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("IP class deinitialized")

    def get_ip4_addresses(self):
        """ Получение IP v4 """
        try:
            self.ipv4_list = []
            for interface in netifaces.interfaces():
                try:
                    for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                        self.ipv4_list.append(link['addr'])
                except:
                    pass
            return self.ipv4_list
        except Exception as e:
            logging.error("Error while getting IP v4: " + str(e))

    def get_ip6_addresses(self):
        """ Получение IP v6 """
        try:
            logging.info("Started task get IP v6")
            self.ipv6_list = []
            for interface in netifaces.interfaces():
                try:
                    for link in netifaces.ifaddresses(interface)[netifaces.AF_INET6]:
                        self.ipv6_list.append(link['addr'])
                except Exception as e:
                    logging.error(str(e) + version)
            return self.ipv6_list
        except Exception as e:
            logging.error("Error while getting IP v6: " + str(e))

    def get_all_ip(self):
        """ Получение IP v4 + v6 """
        return "Your IP v4 is: \n" + str(self.get_ip4_addresses()) + \
                    "\n \nYour IP v6 is:\n" + str(self.get_ip6_addresses())

class Port:
    """ Класс для работы с портами"""
    def __init__(self):
        """ Инициализация """
        self.open_ports = []
        self.first_port = 0
        self.end_port = 0
        logging.info("Port class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("Port class deinitialized")

    def scan_port(self, host, port):
        """Проверяет, открыт ли порт на заданном хосте."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Устанавливаем таймаут в 1 секунду
            result = sock.connect_ex((host, port))
            return port, result == 0  # Если результат 0, порт открыт

    def scan_ports(self, host, start_port, end_port):
        """Сканирует порты в заданном диапазоне."""
        try:
            logging.info("Started scan ports")
            with ThreadPoolExecutor(max_workers=100) as executor:
                futures = {executor.submit(self.scan_port, host, port):
                        port for port in range(start_port, end_port + 1)}
                for future in futures:
                    port, is_open = future.result()
                    if is_open:
                        self.open_ports.append(port)
            return self.open_ports
        except Exception as e:
            logging.error("Error while scan ports: " + str(e))

class Task:
    """ Класс для работы с заданиями"""
    def __init__(self):
        """ Инициализация """
        self.name_task = ""
        logging.info("Task class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("Task class deinitialized")

    def check_task(self, app, ip, port, keyboard):
        """ Проверка задания + нажатия Enter """
        # Проверка Enter
        if keyboard.enter_pressed:
            try:
                if app.task == "ip_ports":
                    ip.task_ip = ''.join(keyboard.get_keys())
                    keyboard.keys_erase()
                    app.draw_text += ip.task_ip + "\nEnter first port: \n"
                    app.task = "ip_first"
                elif app.task == "ip_first":
                    port.first_port = int(''.join(keyboard.get_keys()))
                    keyboard.keys_erase()
                    app.draw_text += str(port.first_port) + "\nEnter end port: \n"
                    app.task = "ip_end"
                elif app.task == "ip_end":
                    port.end_port = int(''.join(keyboard.get_keys()))
                    keyboard.keys_erase()
                    app.task = "ip_ports_start"
                keyboard.enter_pressed = False
            except Exception as e:
                app.exception("Error while perfoming custom task: ", str(e))

        # Вся информация
        if app.task == "all_info":
            try:
                logging.info("Started task 'all info'")
                pr.begin_drawing()
                pr.draw_text("Checking info this may take a while", 550, 125, 10, colors.BLACK)
                pr.clear_background(colors.WHITE)
                pr.end_drawing()
                pr.begin_drawing()
                app.draw_text = "All information: \nNetwork devicess info \n"
                if os.name == 'nt':
                    app.draw_text += subprocess.check_output("ipconfig" ).decode('utf-8')
                else:
                    app.draw_text += subprocess.check_output("ifconfig" ).decode('utf-8')

                app.draw_text += "Checking open ports... \n"
                for ip_l in ip.get_ip4_addresses():
                    open_ports = port.scan_ports(ip_l, 1, 49151)
                    if len(open_ports) != 0:
                        app.draw_text += "Open ports in " + ip_l + \
                            ":" + "\n" + str(open_ports) + "\n \n"
                    else:
                        app.draw_text += 'All ports are closed in ' + ip_l
                app.task = ""
            except Exception as e:
                app.exception("Error while perfoming task 'all info': ", str(e))

        # Проверка портов для кастом
        elif app.task == "ip_ports_start":
            try:
                logging.info("Started custom task")
                app.draw_text += str(port.end_port) + '\nStarting task... \n'
                open_ports = port.scan_ports(ip.task_ip, port.first_port, port.end_port)
                app.draw_text += "Open ports in " + ip.task_ip + \
                    ":" + "\n" + str(open_ports) + "\n"
                app.task = ""
            except Exception as e:
                app.exception("Error while perfoming custom task: ", str(e))

class Keyboard:
    """ Класс для работы с клавиатурой"""
    def __init__(self):
        """ Инициализация """
        self.keys = []
        self.enter_pressed = False
        logging.info("Keyboard class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("Keyboard class deinitialized")

    def get_keys(self):
        """ Получить текст с клавиатуры """
        return self.keys

    def append_keys(self, var):
        """ Добавить текст """
        self.keys.append(var)

    def keys_erase(self):
        """ Очистить клавиатуру """
        self.keys = []

    def keys_del(self):
        """ Удалить 1 смивол с конца"""
        self.keys = self.keys[:-1]

    def check_key(self, app):
        """ Добавление текста с клавиатуры """
        # Получение нажатия всех кнопок с клавиатуры
        while value := pr.get_key_pressed():
            if app.terminal_active:
                if pr.is_key_pressed(257):
                    self.enter_pressed = True
                elif pr.is_key_pressed(259):
                    self.keys_del()
                else:
                    self.keys.append(chr(value))

class App(Keyboard):
    """ Основной класс приложения"""
    def __init__(self):
        """ Инициализация класса """
        super().__init__()
        self.version = version
        self.width = width
        self.height = height
        self.fps = fps
        self.app_name = app_name
        self.draw_text = ""
        self.terminal_active = False
        self.task = ""
        self.first_port = 0
        self.end_port = 0
        logging.info("App class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("App class deinitialized")

    def init_app(self):
        """ Запуск приложения """
        try:
            pr.init_window(self.width, self.height, self.app_name)
            pr.set_target_fps(self.fps)
            pr.set_window_icon(pr.load_image('portscanner.png'))
            logging.info("App initialized")
        except Exception as e:
            logging.critical("Error while initializing App window: " + str(e))

    def draw_main(self):
        """ Отрисовка дизайна приложения """
        pr.draw_line(500,25,500,575,colors.BLACK)
        pr.draw_line(25,575,975,575,colors.BLACK)
        pr.draw_line(25,25,975,25,colors.BLACK)
        pr.draw_text("Select option", 50,50,25,colors.BLACK)
        pr.draw_text("Result", 550,50,25,colors.BLACK)
        pr.draw_text("Enter IP and ports", 50, 175, 15, colors.BLACK)
        pr.draw_rectangle_lines(525, 100, 450, 450, colors.BLACK)
        pr.draw_text(app_name + " by VL_PLAY Games " + version, 725, 585, 12, colors.BLACK)

    def draw_terminal(self , keys):
        """ Отрисовка терминала """
        pr.draw_text(self.draw_text + str(''.join(keys)) if self.terminal_active \
                     else self.draw_text, \
                     550, 125, 10, colors.BLACK)

    def error_init(self, e):
        """ Отрисовка ошибки """
        logging.critical(str(e) + version)
        pr.init_window(300, 200, "Port Scanner Critical Error")
        pr.set_target_fps(30)
        pr.set_window_icon(pr.load_image('portscanner.png'))
        logging.info("Error window initialized")
        while not pr.window_should_close():
            pr.clear_background(colors.WHITE)
            pr.draw_text("Critical Error", 75, 75, 25, colors.BLACK)
            pr.end_drawing()
            pr.begin_drawing()

    def exception(self, text, e):
        """ Обработка исключений """
        logging.error(text)
        logging.error(str(e))
        self.terminal_active = False
        self.task = ""
        self.enter_pressed = False
        self.draw_text += "An error has occurred"

class Button:
    """ Класс для работы с кнопками"""
    def __init__(self):
        """ Инициализация """
        logging.info("Button class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("Button class deinitialized")

    def but_all_info(self, app):
        """ Отрисовка и отработка кнопки вся информация """
        if pr.gui_button(
                pr.Rectangle(350, 100, 100, 50),
                'All info'):   
            app.task = 'all_info'

    def but_custom_task(self, app):
        """ Отрисовка и отработка кнопки кастом """
        if pr.gui_button(
                pr.Rectangle(50, 200, 100, 50),
                'Start'):   
            app.draw_text = "Enter IP address to check: \n"
            app.terminal_active = True
            app.task = "ip_ports"

    def but_main_ports(self, app, ip, port):
        """ Отрисовка и обработка кнопки проверить основные порты """
        # Получение открытых портов собственного IP
        if pr.gui_button(
                    pr.Rectangle(200, 100, 100, 50),
                    'Check main ports'):
            app.task = "main_ports"
            pr.begin_drawing()
            pr.draw_text("Checking open ports...", 550, 125, 10, colors.BLACK)
            pr.clear_background(colors.WHITE)
            pr.end_drawing()
            pr.begin_drawing()
            app.draw_text = "Checking open ports... \n \n"
            for ip_l in ip.get_ip4_addresses():
                open_ports = port.scan_ports(ip_l, 1, 10000)
                if len(open_ports) != 0:
                    app.draw_text += "Open ports in " + ip_l + \
                        ":" + "\n" + str(open_ports) + "\n \n"
                else:
                    app.draw_text += 'All ports are closed in ' + ip_l

    def but_ip(self, app, ip):
        """ Отрисовка и обработка кнопки получения всех ip """
        if pr.gui_button(
                    pr.Rectangle(50, 100, 100, 50),
                    'Check your IP'):
            app.draw_text = ip.get_all_ip()

    def but_next_console(self):
        """ Отрисовка и обработка кнопки следующей страницы терминала """
        if pr.gui_button(
                    pr.Rectangle(950, 550, 25, 25),
                    '>>'):
            pass

    def but_prev_console(self):
        """ Отрисовка и обработка кнопки предыдущей страницы терминала """
        if pr.gui_button(
                    pr.Rectangle(900, 550, 25, 25),
                    '<<'):
            pass

    def check_all_but(self, app, ip, port):
        """ Проверка всех кнопок """
        self.but_all_info(app)
        self.but_custom_task(app)
        self.but_ip(app, ip)
        self.but_main_ports(app, ip, port)
        self.but_next_console()
        self.but_prev_console()

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
    try:
        app.init_app()
        while not pr.window_should_close():
            pr.begin_drawing()
            app.draw_main()
            button.check_all_but(app, ip, port)
            keyboard.check_key(app)
            task.check_task(app, ip, port, keyboard)
            app.draw_terminal(keyboard.get_keys())
            pr.clear_background(colors.WHITE)
            pr.end_drawing()

        pr.close_window()
    except Exception as e:
        app.error_init(e)
    del app, ip, task, port, keyboard, button, terminal
    logging.info("App is closed")

if __name__ == '__main__':
    main()
