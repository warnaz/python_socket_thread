import socket
import concurrent.futures
from utils import port

port = port


def client():
    # Создание объекта сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Подключение к серверу
    server_address = ('localhost', port)
    client_socket.connect(server_address)

    # Отправка данных на сервер
    while True:
        try:
            message = input('Введите сообщение: ')
            client_socket.sendall(message.encode())

            if message in ('exit', 'break', 'quit', 'q'):
                break
        except:
            break

    # Закрытие соединения
    client_socket.close()


# Создание пула потоков
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    # Запуск клиентов
    futures = [executor.submit(client) for _ in range(100)]

    # Ожидание завершения всех клиентов
    concurrent.futures.wait(futures)
