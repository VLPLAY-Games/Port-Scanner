import subprocess
import os
import socket
import logging
from concurrent.futures import ThreadPoolExecutor
import pyray as pr
import netifaces
from raylib import colors
from config import width, height, fps, app_name, version

logging.basicConfig(filename='report.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


class Ip:
    def __init__(self):
        self.ipv4_list = []
        self.ipv6_list = []
    
    # Получение IP v4
    def get_ip4_addresses(self):
        self.ipv4_list = []
        for interface in netifaces.interfaces():
            try:
                for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                    self.ipv4_list.append(link['addr'])
            except:
                pass
        return self.ipv4_list
    
    # Получение IP v6
    def get_ip6_addresses(self):
        self.ipv6_list = []
        for interface in netifaces.interfaces():
            try:
                for link in netifaces.ifaddresses(interface)[netifaces.AF_INET6]:
                    self.ipv6_list.append(link['addr'])
            except Exception as e:
                logging.error(str(e) + version)
        return self.ipv6_list
    
    def get_all_ip(self):
        return "Your IP v4 is: \n" + str(self.get_ip4_addresses()) + \
                    "\n \nYour IP v6 is:\n" + str(self.get_ip6_addresses())
        
class Port:
    def __init__(self):
        self.open_ports = []

    def scan_port(self, host, port):
        """Проверяет, открыт ли порт на заданном хосте."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Устанавливаем таймаут в 1 секунду
            result = sock.connect_ex((host, port))
            return port, result == 0  # Если результат 0, порт открыт

    def scan_ports(self, host, start_port, end_port):
        """Сканирует порты в заданном диапазоне."""
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = {executor.submit(self.scan_port, host, port):
                    port for port in range(start_port, end_port + 1)}
            for future in futures:
                port, is_open = future.result()
                if is_open:
                    self.open_ports.append(port)
        return self.open_ports


class Task():
    def __init__(self):
        self.name_task = ""
    
class Keyboard:
    def __init__(self):
        self.keys = []
    
    def get_keys(self):
        return self.keys
    
    def append_keys(self, var):
        self.keys.append(var)

    def keys_erase(self):
        self.keys = []



class App(Keyboard):
    def __init__(self):
        self.version = version
        self.width = width
        self.height = height
        self.fps = fps
        self.app_name = app_name
        self.draw_text = ""
        self.terminal_active = False
        self.enter_pressed = False
        self.task = ""
        self.first_port = 0
        self.end_port = 0
    
    def init_app(self):
        pr.init_window(self.width, self.height, self.app_name)
        pr.set_target_fps(self.fps)
        pr.set_window_icon(pr.load_image('portscanner.png'))

    def draw_main(self):
        pr.draw_line(500,25,500,575,colors.BLACK)
        pr.draw_line(25,575,975,575,colors.BLACK)
        pr.draw_line(25,25,975,25,colors.BLACK)
        pr.draw_text("Select option", 50,50,25,colors.BLACK)
        pr.draw_text("Result", 550,50,25,colors.BLACK)
        pr.draw_text("Enter IP and ports", 50, 175, 15, colors.BLACK)
        pr.draw_rectangle_lines(525, 100, 450, 450, colors.BLACK)
        pr.draw_text(app_name + " by VL_PLAY Games " + version, 725, 585, 12, colors.BLACK)

    def draw_terminal(self , keys):
        pr.draw_text(self.draw_text + str(''.join(keys)) if self.terminal_active else self.draw_text, \
                     550, 125, 10, colors.BLACK)
        
    def error_init(self, e):
        logging.critical(str(e) + version)
        pr.init_window(300, 200, "Port Scanner Critical Error")
        pr.set_target_fps(30)
        pr.set_window_icon(pr.load_image('portscanner.png'))
        while not pr.window_should_close():
            pr.clear_background(colors.WHITE)
            pr.draw_text("Critical Error", 75, 75, 25, colors.BLACK)
            pr.end_drawing()
            pr.begin_drawing()
        

class Button:
    def __init__(self):
        pass


def main():
    logging.info("App started")
    app = App()
    ip = Ip()
    task = Task()
    port = Port()
    keyboard = Keyboard()
    try:
        app.init_app()

        task_ip = ""
        while not pr.window_should_close():
            pr.begin_drawing()

            app.draw_main()

            # Получение IP адреса
            if pr.gui_button(
                        pr.Rectangle(50, 100, 100, 50),
                        'Check your IP'):
                app.draw_text = ip.get_all_ip()

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
                        app.draw_text += "Open ports in " + ip_l + ":" + "\n" + str(open_ports) + "\n \n"
                    else:
                        app.draw_text += 'All ports are closed in ' + ip_l


            # Получение полной информации
            if pr.gui_button(
                        pr.Rectangle(350, 100, 100, 50),
                        'All info'):   
                app.task = 'all_info'

            # Получение IP адреса
            if pr.gui_button(
                        pr.Rectangle(50, 200, 100, 50),
                        'Start'):   
                app.draw_text = "Enter IP address to check: \n"
                app.terminal_active = True
                app.task = "ip_ports"

            # Получение нажатия всех кнопок с клавиатуры
            while value := pr.get_key_pressed():
                if app.terminal_active:
                    if pr.is_key_pressed(257):
                        app.enter_pressed = True
                    else:
                        keyboard.keys.append(chr(value))
            try:
                if app.enter_pressed:
                    if app.task == "ip_ports":
                        app.task_ip = ''.join(keyboard.get_keys())
                        keyboard.keys_erase()
                        app.draw_text += task_ip + "\nEnter first port: \n"
                        app.task = "ip_first"
                    elif app.task == "ip_first":
                        first_port = int(''.join(keyboard.get_keys()))
                        keyboard.keys_erase()
                        app.draw_text += str(first_port) + "\nEnter end port: \n"
                        app.task = "ip_end"
                    elif app.task == "ip_end":
                        end_port = int(''.join(keyboard.get_keys()))
                        keyboard.keys_erase()
                        app.task = "ip_ports_start"

                    app.enter_pressed = False
            except Exception as e:
                logging.error(str(e) + version)
                app.terminal_active = False
                app.task = ""
                app.enter_pressed = False
                app.draw_text += "An error has occurred"
            # Проверка задания
            try:
                if app.task == "ip_ports_start":
                    app.draw_text += str(end_port) + '\nStarting task... \n'
                    open_ports = port.scan_ports(task_ip, first_port, end_port)
                    app.draw_text += "Open ports in " + task_ip + ":" + "\n" + str(open_ports) + "\n"
                    app.task = ""
                elif app.task == "all_info":
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
                            app.draw_text += "Open ports in " + ip_l + ":" + "\n" + str(open_ports) + "\n \n"
                        else:
                            app.draw_text += 'All ports are closed in ' + ip_l
                    app.task = ""
            except Exception as e:
                logging.error(str(e) + version)
                app.terminal_active = False
                app.draw_text += "An error has occurred"
                app.task = ""

            app.draw_terminal(keyboard.get_keys())
            pr.clear_background(colors.WHITE)
            pr.end_drawing()

        pr.close_window()
    except Exception as e:
        app.error_init(e)
    logging.info("App is closed")
        

if __name__ == '__main__':
    main()
