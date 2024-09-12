import socket, pyray as pr
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

def main():
    width = 1000
    height = 600
    draw_text = ""
    margin = 0
    pr.init_window(width, height, "Port Scanner")
    pr.set_target_fps(60)


    pr.set_window_icon(pr.load_image('portscanner.png'))
    IP = socket.gethostbyname(socket.gethostname())
    while not pr.window_should_close():
        pr.begin_drawing()

        pr.draw_line(500,25,500,575,colors.BLACK)
        pr.draw_line(25,575,975,575,colors.BLACK)
        pr.draw_line(25,25,975,25,colors.BLACK)
        
        pr.draw_text("Select option", 50,50,25,colors.BLACK)
        pr.draw_text("Result", 550,50,25,colors.BLACK)

        pr.draw_rectangle_lines(525, 100, 450, 450, colors.BLACK)

        # Получение IP адреса
        if pr.gui_button(
                    pr.Rectangle(50, 100, 100, 50), 
                    'Check your IP'):   
                draw_text = "Your IP is: "+ IP

        # Получение открытых портов собственного IP 
        if pr.gui_button(
                    pr.Rectangle(200, 100, 100, 50), 
                    'Check ports (1000)'): 
                open_ports = scan_ports(IP, 1, 1000)
                if len(open_ports) != 0:
                    draw_text = "Open ports: " + str(open_ports)
                else:
                    draw_text = 'All ports are closed'
                
                    
        pr.draw_text(draw_text, 550, 125, 10, colors.BLACK)
        pr.clear_background(colors.WHITE)
        pr.end_drawing()
    pr.close_window()



if __name__ == '__main__':
    main()



    # target_host = input("Введите IP-адрес или доменное имя: ")
    # start_port = int(input("Введите начальный порт: "))
    # end_port = int(input("Введите конечный порт: "))
    
    # print(f"Сканирование портов от {start_port} до {end_port} на {target_host}...")
    # open_ports = scan_ports(target_host, start_port, end_port)
    
    # print("\nОткрытые порты:")
    # for port in open_ports:
    #     print(port)