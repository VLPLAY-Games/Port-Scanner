import socket, pyray
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
                print(f"Порт {port} открыт.")
            else:
                print(f"Порт {port} закрыт.")
    return open_ports

def main():
    width = 1000
    height = 600
    pyray.init_window(width, height, "Port Scanner")
    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(colors.WHITE)
        if pyray.gui_button(
                    pyray.Rectangle(100, 100, 100, 50), 
                    'Press me!'):
                print('Кнопка нажата')
        pyray.end_drawing()
    pyray.close_window()



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