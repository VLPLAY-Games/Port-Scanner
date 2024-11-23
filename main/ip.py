""" Файл для работы с IP"""

import logging
import os
from ipaddress import ip_address, ip_network
import netifaces
from config import VERSION
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

class Ip:
    """ Класс для работы с IP """
    def __init__(self):
        """ Инициализация """
        self.ipv4_list = []
        self.ipv6_list = []
        self.task_ip = ""
        self.status = ""
        self.result = []
        logging.info("IP class initialized")

    def __del__(self):
        """ Деинициализация """
        logging.info("IP class deinitialized")

    def get_ip4_addresses(self):
        """ Получение IP v4 """
        try:
            logging.info("Started task 'get IP v4'")
            self.ipv4_list = []
            for interface in netifaces.interfaces():
                try:
                    for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                        self.ipv4_list.append(link['addr'])
                except Exception as e:
                    logging.error(str(e) + VERSION)
            logging.info("Finished task 'get IP v4'")
            return self.ipv4_list
        except Exception as e:
            logging.error("Error while getting IP v4: " + str(e))

    def get_ip6_addresses(self):
        """ Получение IP v6 """
        try:
            logging.info("Started task 'get IP v6'")
            self.ipv6_list = []
            for interface in netifaces.interfaces():
                try:
                    for link in netifaces.ifaddresses(interface)[netifaces.AF_INET6]:
                        self.ipv6_list.append(link['addr'])
                except Exception as e:
                    logging.error(str(e) + VERSION)
            logging.info("Finished task 'get IP v6'")
            return self.ipv6_list
        except Exception as e:
            logging.error("Error while getting IP v6: " + str(e))

    def get_all_ip(self, app, terminal, task):
        """ Получение IP v4 + v6 """
        try:
            logging.info("Started task 'get all ip'")
            task.status = "WORK"
            self.result.append("Your IP v4 is: \n")
            for ip in self.get_ip4_addresses():
                self.result.append(ip)
            self.result.append("\n \nYour IP v6 is:\n")
            for ip in self.get_ip6_addresses():
                self.result.append(ip)
            return self.result

        except Exception as e:
            self.status = "ERR"
            app.exception("Error while perfoming task 'all info': ", str(e), terminal, task)

    def check_ip(self, ip):
        """ Проверка правильности написания ip адреса"""
        try:
            ip_address(ip)
        except Exception as e:
            logging.warning("IP Adress is not valid " + str(e))
            return "IP Adress is not valid"
        return "OK"
    
    def ping(self, terminal, task):
        """ Функция пинга """
        parameter = '-n' if os.name == 'nt' else '-c'
        command = ['ping', parameter, '5', self.task_ip]
        try:
            terminal.draw_text += subprocess.check_output(command).decode("utf-8")
            task.status = "OK"
            logging.info("Ping successfull")
        except Exception as e:
            terminal.draw_text += "\nAn error was occured"
            task.status = "ERR"
            logging.error("Error while pinging " + self.task_ip + " " + str(e))
        logging.info("Ping command completed")

    def ping_device(self, ip):
        try:
            subprocess.check_output(f"ping -c 1 -W 1 {ip}", shell=True)
            return ip
        except subprocess.CalledProcessError:
            return None

    def active_devices(self, terminal, task):
        active_ips = []
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = {executor.submit(self.ping_device, str(ip)): str(ip) for ip in ip_network(self.task_ip, False)}
            for future in futures:
                ip = future.result()
                if ip: 
                    active_ips.append(ip)
        if active_ips:
            terminal.draw_text += f"Found {len(active_ips)} active devices: \n"
            for active in active_ips:
                terminal.draw_text += active + "\n"
        else:
            terminal.draw_text += "No active devices found"
        task.status = "OK" if active_ips else "ERR"