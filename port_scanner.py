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

def scan_port(host, port):
    """Проверяет, открыт ли порт на заданном хосте."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)  # Устанавливаем таймаут в 1 секунду
        result = sock.connect_ex((host, port))
        return port, result == 0  # Если результат 0, порт открыт

def scan_ports(host, start_port, end_port):
    """Сканирует порты в заданном диапазоне."""
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, host, port):
                   port for port in range(start_port, end_port + 1)}
        for future in futures:
            port, is_open = future.result()
            if is_open:
                open_ports.append(port)
                # print(f"Порт {port} открыт.")
            else:
                pass
                # print(f"Порт {port} закрыт.")
    return open_ports

# Получение IP v4
def get_ip4_addresses():
    ip_list = []
    for interface in netifaces.interfaces():
        try:
            for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                ip_list.append(link['addr'])
        except:
            pass
    return ip_list

# Получение IP v6
def get_ip6_addresses():
    ip_list = []
    for interface in netifaces.interfaces():
        try:
            for link in netifaces.ifaddresses(interface)[netifaces.AF_INET6]:
                ip_list.append(link['addr'])
        except Exception as e:
            logging.error(str(e) + version)
    return ip_list

def main():
    draw_text = ""
    terminal_active = False
    keys = []
    enter_pressed = False
    task = ""
    first_port = 0
    end_port = 0
    pr.init_window(width, height, app_name)
    pr.set_target_fps(fps)


    pr.set_window_icon(pr.load_image('portscanner.png'))
    task_ip = ""
    while not pr.window_should_close():
        pr.begin_drawing()

        pr.draw_line(500,25,500,575,colors.BLACK)
        pr.draw_line(25,575,975,575,colors.BLACK)
        pr.draw_line(25,25,975,25,colors.BLACK)

        pr.draw_text("Select option", 50,50,25,colors.BLACK)
        pr.draw_text("Result", 550,50,25,colors.BLACK)
        pr.draw_text("Enter IP and ports", 50, 175, 15, colors.BLACK)

        pr.draw_rectangle_lines(525, 100, 450, 450, colors.BLACK)

        # Получение IP адреса
        if pr.gui_button(
                    pr.Rectangle(50, 100, 100, 50),
                    'Check your IP'):
            draw_text = "Your IP v4 is: \n" + str(get_ip4_addresses()) + \
                "\n \nYour IP v6 is:\n" + str(get_ip6_addresses())

        # Получение открытых портов собственного IP
        if pr.gui_button(
                    pr.Rectangle(200, 100, 100, 50),
                    'Check main ports'):
            task = "main_ports"
            pr.begin_drawing()
            pr.draw_text("Checking open ports...", 550, 125, 10, colors.BLACK)
            pr.clear_background(colors.WHITE)
            pr.end_drawing()
            pr.begin_drawing()
            draw_text = "Checking open ports... \n \n"
            for ip in get_ip4_addresses():
                open_ports = scan_ports(ip, 1, 10000)
                if len(open_ports) != 0:
                    draw_text += "Open ports in " + ip + ":" + "\n" + str(open_ports) + "\n \n"
                else:
                    draw_text += 'All ports are closed in ' + ip


        # Получение полной информации
        if pr.gui_button(
                    pr.Rectangle(350, 100, 100, 50),
                    'All info'):   
            task = 'all_info'

        # Получение IP адреса
        if pr.gui_button(
                    pr.Rectangle(50, 200, 100, 50),
                    'Start'):   
            draw_text = "Enter IP address to check: \n"
            terminal_active = True
            task = "ip_ports"

        # Получение нажатия всех кнопок с клавиатуры
        while value := pr.get_key_pressed():
            if terminal_active:
                if pr.is_key_pressed(257):
                    enter_pressed = True
                else:
                    keys.append(chr(value))
        try:
            if enter_pressed:
                if task == "ip_ports":
                    task_ip = ''.join(keys)
                    keys = []
                    draw_text += task_ip + "\nEnter first port: \n"
                    task = "ip_first"
                elif task == "ip_first":
                    first_port = int(''.join(keys))
                    keys = []
                    draw_text += str(first_port) + "\nEnter end port: \n"
                    task = "ip_end"
                elif task == "ip_end":
                    end_port = int(''.join(keys))
                    keys = []
                    task = "ip_ports_start"

                enter_pressed = False
        except Exception as e:
            logging.error(str(e) + version)
            terminal_active = False
            task = ""
            enter_pressed = False
            draw_text += "An error has occurred"
        # Проверка задания
        try:
            if task == "ip_ports_start":
                draw_text += str(end_port) + '\nStarting task... \n'
                open_ports = scan_ports(task_ip, first_port, end_port)
                draw_text += "Open ports in " + task_ip + ":" + "\n" + str(open_ports) + "\n"
                task = ""
            elif task == "all_info":
                pr.begin_drawing()
                pr.draw_text("Checking info this may take a while", 550, 125, 10, colors.BLACK)
                pr.clear_background(colors.WHITE)
                pr.end_drawing()
                pr.begin_drawing()
                draw_text = "All information: \nNetwork devicess info \n"
                if os.name == 'nt':
                    draw_text += subprocess.check_output("ipconfig" ).decode('utf-8')
                else:
                    draw_text += subprocess.check_output("ifconfig" ).decode('utf-8')

                draw_text += "Checking open ports... \n"
                for ip in get_ip4_addresses():
                    open_ports = scan_ports(ip, 1, 49151)
                    if len(open_ports) != 0:
                        draw_text += "Open ports in " + ip + ":" + "\n" + str(open_ports) + "\n \n"
                    else:
                        draw_text += 'All ports are closed in ' + ip
                task = ""
        except Exception as e:
            logging.error(str(e) + version)
            terminal_active = False
            draw_text += "An error has occurred"
            task = ""

        pr.draw_text(app_name + " by VL_PLAY Games " + version, 725, 585, 12, colors.BLACK)
        pr.draw_text(draw_text + str(''.join(keys)) if terminal_active else draw_text, \
                     550, 125, 10, colors.BLACK)
        pr.clear_background(colors.WHITE)
        pr.end_drawing()

    pr.close_window()



if __name__ == '__main__':
    try:
        logging.info("App started")
        main()
    except Exception as e:
        logging.critical(str(e) + version)
        pr.init_window(300, 200, "Port Scanner Critical Error")
        pr.set_target_fps(30)
        pr.set_window_icon(pr.load_image('portscanner.png'))
        while not pr.window_should_close():
            pr.clear_background(colors.WHITE)
            pr.draw_text("Critical Error", 75, 75, 25, colors.BLACK)
            pr.end_drawing()
            pr.begin_drawing()
    logging.info("App is closed")
