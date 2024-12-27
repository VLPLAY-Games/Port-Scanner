""" Файл для работы с портами"""

import logging
from socket import socket, AF_INET, SOCK_STREAM
from concurrent.futures import ThreadPoolExecutor

class Port:
    """ Класс для работы с портами"""
    def __init__(self):
        """ Инициализация """
        logging.info("Started Port class initializing")
        self.open_ports = []
        self.first_port = 0
        self.end_port = 0
        logging.info("Port class initialized successfully")

    def __del__(self):
        """ Деинициализация """
        logging.info("Port class deinitialized")

    def scan_port(self, host, port):
        """Проверяет, открыт ли порт на заданном хосте."""
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.settimeout(0.01)
            result = sock.connect_ex((host, port))
            return port, result == 0

    def scan_ports(self, host, start_port, end_port):
        """Сканирует порты в заданном диапазоне."""
        try:
            logging.info("Started task 'scan ports'")
            self.open_ports = []
            with ThreadPoolExecutor(max_workers=100) as executor:
                futures = {executor.submit(self.scan_port, host, port):
                        port for port in range(start_port, end_port + 1)}
                for future in futures:
                    port, is_open = future.result()
                    if is_open:
                        self.open_ports.append(port)
            logging.info("Finished task 'scan ports'")
            return self.open_ports
        except Exception as e:
            logging.error("Error while scan ports: %s", str(e))
            return []


    def scan_all_ports(self, pr, colors, app, ip, terminal, task, language, settings):
        """ Сканирование всех портов на всех IP"""
        try:
            logging.info("Started task 'All ports'")
            task.status = "WORK"
            app.fast_draw_text("Checking open ports...", \
                               pr, colors, terminal, task, language, settings)
            terminal.draw_text = "Checking open ports... \n \n"
            for ip_l in ip.get_ip4_addresses():
                terminal.draw_text += "Open ports in " + ip_l + ":\n"
                app.fast_draw_text(terminal.draw_text, pr, \
                                   colors, terminal, task, language, settings)
                self.open_ports = self.scan_ports(ip_l, 1, 49151)
                if len(self.open_ports) != 0:
                    terminal.draw_text += str(self.open_ports)[1:-1] + "\n \n"
                    app.fast_draw_text(terminal.draw_text, \
                                       pr, colors, terminal, task, language, settings)
                    self.open_ports = []
                else:
                    terminal.draw_text += 'All ports are closed in ' + ip_l
                    app.fast_draw_text(terminal.draw_text, \
                                       pr, colors, terminal, task, language, settings)
            task.status = "OK"
        except Exception as e:
            task.status = "ERR"
            app.exception("Error while perfoming task 'All ports': ", str(e), terminal, task)
        task.task = ""

    def check_port_num(self, port):
        """ Проверка на большое и маленькое число порта"""
        if port > 65535:
            logging.warning("Port is too big")
            return "Port is too big"
        if port < 1:
            logging.warning("Port cannot be smaller than 1")
            return "Port cannot be smaller than 1"
        return "OK"
