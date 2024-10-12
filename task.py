""" Файл для работы с задачами"""

import logging
import subprocess
import os

class Task:
    """ Класс для работы с заданиями"""
    def __init__(self):
        """ Инициализация """
        self.name_task = ""
        self.task = ""
        self.status = ""
        logging.info("Task class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("Task class deinitialized")

    def check_task(self, app, ip, port, keyboard, pr, colors, terminal, task):
        """ Проверка задания + нажатия Enter """
        # Проверка Enter
        if keyboard.enter_pressed:
            try:
                if self.task == "ip_ports":
                    ip.task_ip = ''.join(keyboard.get_keys())
                    keyboard.keys_erase()
                    terminal.draw_text += ip.task_ip + "\nEnter first port: \n"
                    self.task = "ip_first"
                elif self.task == "ip_first":
                    port.first_port = int(''.join(keyboard.get_keys()))
                    keyboard.keys_erase()
                    self.status = port.check_port_num(port.first_port)

                    if self.status == "OK":
                        terminal.draw_text += str(port.first_port) + "\nEnter end port: \n"
                        self.task = "ip_end"
                    else:
                        terminal.draw_text += str(port.first_port) + \
                            "\n" + self.status + ". Try again"
                        self.task = ""
                        terminal.terminal_active = False
                elif self.task == "ip_end":
                    port.end_port = int(''.join(keyboard.get_keys()))
                    keyboard.keys_erase()

                    self.status = port.check_port_num(port.end_port)

                    if self.status == "OK":
                        self.task = "ip_ports_start"
                    else:
                        terminal.draw_text += str(port.end_port) + \
                            "\n" + self.status + ". Try again"
                        self.task = ""
                        terminal.terminal_active = False

                keyboard.enter_pressed = False
            except Exception as e:
                app.exception("Error while perfoming custom task: ", str(e),terminal, task)

        # Вся информация
        if self.task == "all_info":
            try:
                logging.info("Started task 'all info'")
                pr.begin_drawing()
                pr.draw_text("Checking info this may take a while", 550, 125, 10, colors.BLACK)
                pr.clear_background(colors.WHITE)
                pr.end_drawing()
                pr.begin_drawing()
                terminal.draw_text = "All information: \nNetwork devicess info \n"
                if os.name == 'nt':
                    terminal.draw_text += subprocess.check_output("ipconfig" ).decode('utf-8')
                else:
                    terminal.draw_text += subprocess.check_output("ifconfig" ).decode('utf-8')

                terminal.draw_text += "Checking open ports... \n"
                for ip_l in ip.get_ip4_addresses():
                    port.open_ports = port.scan_ports(ip_l, 1, 49151)
                    if len(port.open_ports) != 0:
                        terminal.draw_text += "Open ports in " + ip_l + \
                            ":" + "\n" + str(port.open_ports)[1:-1] + "\n \n"
                    else:
                        terminal.draw_text += 'All ports are closed in ' + ip_l
            except Exception as e:
                app.exception("Error while perfoming task 'all info': ", str(e))
            self.task = ""

        # Проверка портов для кастом
        elif self.task == "ip_ports_start":
            try:
                logging.info("Started custom task")
                terminal.draw_text += str(port.end_port) + '\nStarting task... \n'
                open_ports = port.scan_ports(ip.task_ip, port.first_port, port.end_port)
                terminal.draw_text += "Open ports in " + ip.task_ip + \
                    ":" + "\n" + str(open_ports)[1:-1] + "\n"
            except Exception as e:
                app.exception("Error while perfoming custom task: ", str(e), self)
            self.task = ""

        elif self.task == "all_ports":
            port.scan_all_ports(pr, colors, app, ip, terminal, task)
