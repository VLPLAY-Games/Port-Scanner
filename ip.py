import netifaces
import logging
from config import version

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
        return "Your IP v4 is: \n" + str(self.get_ip4_addresses())[1:-1] + \
                    "\n \nYour IP v6 is:\n" + str(self.get_ip6_addresses())[1:-1]