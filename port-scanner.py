import socket, pyray as pr, netifaces, subprocess, os
from raylib import colors
from concurrent.futures import ThreadPoolExecutor

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
        futures = {executor.submit(scan_port, host, port): port for port in range(start_port, end_port + 1)}
        for future in futures:
            port, is_open = future.result()
            if is_open:
                open_ports.append(port)
                # print(f"Порт {port} открыт.")
            else:
                pass
                # print(f"Порт {port} закрыт.")
    return open_ports


def get_ip4_addresses():
    ip_list = []
    for interface in netifaces.interfaces():
        for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
            ip_list.append(link['addr'])
    return ip_list

def get_ip6_addresses():
    ip_list = []
    for interface in netifaces.interfaces():
        for link in netifaces.ifaddresses(interface)[netifaces.AF_INET6]:
            ip_list.append(link['addr'])
    return ip_list


def main():
    width = 1000
    height = 600
    draw_text = ""
    pr.init_window(width, height, "Port Scanner")
    pr.set_target_fps(30)


    pr.set_window_icon(pr.load_image('portscanner.png'))
    IP = socket.gethostbyname(socket.gethostname())
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
                draw_text = "Your IP v4 is: \n" + str(get_ip4_addresses()) + "\n \n" + "Your IP v6 is:" + "\n" + str(get_ip6_addresses())
                
        # Получение открытых портов собственного IP 
        if pr.gui_button(
                    pr.Rectangle(200, 100, 100, 50), 
                    'Check main ports'): 
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

                
        pr.draw_text(draw_text, 550, 125, 10, colors.BLACK)
        pr.clear_background(colors.WHITE)
        pr.end_drawing()
    pr.close_window()



if __name__ == '__main__':
    main()
