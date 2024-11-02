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
        self.check = ""
        logging.info("Task class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("Task class deinitialized")

    def check_task(self, app, ip, port, keyboard, pr, colors, terminal, task, language):
        """ Проверка задания + нажатия Enter """
        # Проверка Enter
        if keyboard.enter_pressed:
            try:
                if self.task == "ip_ports":
                    ip.task_ip = ''.join(keyboard.get_keys())
                    keyboard.keys_erase()
                    self.check = ip.check_ip(ip.task_ip)

                    if self.check == "OK":
                        terminal.draw_text += ip.task_ip + "\nEnter first port: \n"
                        self.task = "ip_first"
                    else:
                        terminal.draw_text += str(ip.task_ip) + \
                            "\n" + self.check + ". Try again"
                        self.task = ""
                        terminal.terminal_active = False

                elif self.task == "ip_first":
                    port.first_port = int(''.join(keyboard.get_keys()))
                    keyboard.keys_erase()
                    self.check = port.check_port_num(port.first_port)

                    if self.check == "OK":
                        terminal.draw_text += str(port.first_port) + "\nEnter end port: \n"
                        self.task = "ip_end"
                    else:
                        terminal.draw_text += str(port.first_port) + \
                            "\n" + self.check + ". Try again"
                        self.task = ""
                        terminal.terminal_active = False
                elif self.task == "ip_end":
                    port.end_port = int(''.join(keyboard.get_keys()))
                    keyboard.keys_erase()

                    self.check = port.check_port_num(port.end_port)

                    if self.check == "OK":
                        self.task = "ip_ports_start"
                    else:
                        terminal.draw_text += str(port.end_port) + \
                            "\n" + self.check + ". Try again"
                        self.task = ""
                        terminal.terminal_active = False

                keyboard.enter_pressed = False
            except Exception as e:
                app.exception("Error while perfoming custom task: ", str(e),terminal, task)

        # Вся информация
        if self.task == "all_info":
            try:
                logging.info("Started task 'all info'")
                self.status = "WORK"
                app.fast_draw_text("Checking info this may take a while", \
                                   pr, colors, terminal, task, language)
                terminal.draw_text = "All information: \nNetwork devicess info \n"
                app.fast_draw_text(terminal.draw_text, pr, colors, terminal, task, language)
                logging.info("Started task 'get ip config'")
                if os.name == 'nt':
                    terminal.draw_text += subprocess.check_output("ipconfig" ).decode('utf-8')
                else:
                    terminal.draw_text += subprocess.check_output("ifconfig" ).decode('utf-8')
                logging.info("Finished task 'get ip config'")
                terminal.draw_text += "Checking open ports... \n"
                app.fast_draw_text(terminal.draw_text, pr, colors, terminal, task, language)
                for ip_l in ip.get_ip4_addresses():
                    terminal.draw_text += "Open ports in " + ip_l + ":\n"
                    app.fast_draw_text(terminal.draw_text, pr, colors, terminal, task, language)
                    port.open_ports = port.scan_ports(ip_l, 1, 49151)
                    if len(port.open_ports) != 0:
                        terminal.draw_text += str(port.open_ports)[1:-1] + "\n \n"
                        app.fast_draw_text(terminal.draw_text, pr, colors, terminal, task, language)
                        port.open_ports = []
                    else:
                        terminal.draw_text += 'All ports are closed in ' + ip_l
                        app.fast_draw_text(terminal.draw_text, pr, colors, terminal, task, language)
                self.status = "OK"
            except Exception as e:
                self.status = "ERR"
                app.exception("Error while perfoming task 'all info': ", str(e), terminal, task)
            self.task = ""

        # Проверка портов для кастом
        elif self.task == "ip_ports_start":
            try:
                logging.info("Started custom task")
                task.status = "WORK"
                app.fast_draw_text(terminal.draw_text, pr, colors, terminal, task, language)
                terminal.draw_text += str(port.end_port) + \
                    '\nStarting task... \nOpen ports in ' + ip.task_ip + ":\n"
                app.fast_draw_text(terminal.draw_text, pr, colors, terminal, task, language)
                open_ports = port.scan_ports(ip.task_ip, port.first_port, port.end_port)
                terminal.draw_text += "\n"
                if len(open_ports) != 0:
                    terminal.draw_text += str(open_ports)[1:-1] + "\n"
                else:
                    terminal.draw_text += "All ports are closed in: " + ip.task_ip +"\n"
                task.status = "OK"
            except Exception as e:
                task.status = "ERR"
                app.exception("Error while perfoming custom task: ", str(e), self)
            self.task = ""

        elif self.task == "all_ports":
            port.scan_all_ports(pr, colors, app, ip, terminal, task, language)