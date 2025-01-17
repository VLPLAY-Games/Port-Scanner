""" Файл для работы с IP"""

import logging
from os import name, path
from ipaddress import ip_address, ip_network
from subprocess import check_output, CalledProcessError
from concurrent.futures import ThreadPoolExecutor
from netifaces import interfaces, ifaddresses, AF_INET, AF_INET6
from config import VERSION
from cffi import FFI

class Ip:
    """ Класс для работы с IP """
    def __init__(self):
        """ Инициализация """
        logging.info("Started Ip class initializing")
        self.ipv4_list = []
        self.ipv6_list = []
        self.task_ip = ""
        self.status = ""
        self.result = []
        self.ffi = FFI()
        self.device_name_lib = self.ffi.dlopen(path.abspath("dll/device_name.dll")) \
                if name == "nt" else self.ffi.dlopen(path.abspath("dll/device_name.so"))
        self.ffi.cdef("""
            const char* get_device_name(const char* ip);
        """)
        logging.info("IP class initialized successfully")

    def __del__(self):
        """ Деинициализация """
        logging.info("IP class deinitialized")

    def get_ip4_addresses(self):
        """ Получение IP v4 """
        try:
            logging.info("Started task 'get IP v4'")
            self.ipv4_list = []
            for interface in interfaces():
                try:
                    for link in ifaddresses(interface)[AF_INET]:
                        self.ipv4_list.append(link['addr'])
                except Exception as e:
                    logging.error("%s %s", str(e), VERSION)
            logging.info("Finished task 'get IP v4'")
            return self.ipv4_list
        except Exception as e:
            logging.error("Error while getting IP v4: %s", str(e))
            return None

    def get_ip6_addresses(self):
        """ Получение IP v6 """
        try:
            logging.info("Started task 'get IP v6'")
            self.ipv6_list = []
            for interface in interfaces():
                try:
                    for link in ifaddresses(interface)[AF_INET6]:
                        self.ipv6_list.append(link['addr'])
                except Exception as e:
                    logging.error("%s %s", str(e), VERSION)
            logging.info("Finished task 'get IP v6'")
            return self.ipv6_list
        except Exception as e:
            logging.error("Error while getting IP v6: %s", str(e))
            return None

    def get_all_ip(self, app, terminal, task):
        """ Получение IP v4 + v6 """
        try:
            logging.info("Started task 'get all ip'")
            task.status = "WORK"
            self.result = []
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
            return None

    def check_ip(self, ip):
        """ Проверка правильности написания ip адреса"""
        try:
            ip_address(ip)
        except Exception as e:
            logging.warning("IP Adress is not valid: %s", str(e))
            return "IP Adress is not valid"
        return "OK"

    def ping(self, terminal, task):
        """ Функция пинга """
        parameter = '-n' if name == 'nt' else '-c'
        command = ['ping', parameter, '5', self.task_ip]
        try:
            terminal.draw_text += check_output(command, shell=name == 'nt').decode("utf-8")

            task.status = "OK"
            logging.info("Ping successfull")
        except Exception as e:
            terminal.draw_text += "\nAn error was occured"
            task.status = "ERR"
            logging.error("Error while pinging %s: %s", self.task_ip, str(e))
        logging.info("Ping command completed")

    def ping_device(self, ip):
        """ Пропинговать IP """
        try:
            parameter = '-n' if name == 'nt' else '-c'
            command = ['ping', parameter, '1', ip]
            temp = check_output(command, shell=name == 'nt')
            if 'Destination host unreachable' in str(temp):
                return None
            return ip
        except CalledProcessError:
            return None

    def get_mac_address(self, ip):
        """ Получить мак адрес устройства """
        try:
            # Выполняем arp для получения MAC-адреса
            command = ['arp', '-a', ip] if name == 'nt' else ['arp', ip]
            output = check_output(command, shell=name == 'nt').decode()

            for line in output.splitlines():
                if ip in line:
                    # Предполагаем, что MAC-адрес находится в формате XX:XX:XX:XX:XX:XX
                    parts = line.split()
                    if len(parts) >= 3:
                        return (parts[1] if name == 'nt' else parts[2])  # Возвращаем MAC-адрес
            return None
        except CalledProcessError:
            return None

    def get_device_name(self, ip):
        """Обертка для вызова функции C++"""
        # Вызов функции C++
        result = self.device_name_lib.get_device_name(ip.encode('utf-8'))
        if result:
            return self.ffi.string(result).decode('utf-8')
        return None

    def active_devices(self, terminal, task):
        """ Найти активные устройства в локальной сети"""
        active_devices_info = []

        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = {executor.submit(self.ping_device, str(ip)): \
                       str(ip) for ip in ip_network(self.task_ip, False)}

            for future in futures:
                ip = future.result()
                if ip:
                    mac_address = self.get_mac_address(ip)
                    device_name = self.get_device_name(ip)
                    active_devices_info.append((ip, mac_address, device_name))

        if active_devices_info:
            terminal.draw_text += f"Found {len(active_devices_info)} active devices: \n"
            for ip, mac, name_i in active_devices_info:
                terminal.draw_text += f"IP: {ip}, MAC: {mac if mac else 'N/A'},\
                      Name: {name_i if name_i else 'N/A'}\n"
        else:
            terminal.draw_text += "No active devices found"

        task.status = "OK" if active_devices_info else "ERR"
