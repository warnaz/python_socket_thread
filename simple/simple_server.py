import socket
from utils import port


def sync_socket_server():
    # Создание объекта сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязка сокета к адресу и порту
    server_address = ('localhost', port)
    server_socket.bind(server_address)

    # Прослушивание входящих соединений
    server_socket.listen()
    print('Сервер запущен и ожидает подключения клиентов...')

    while True:
        # Принятие входящего соединения
        client_socket, client_address = server_socket.accept()
        print(f'Новое подключение от {client_address}')

        # Получение данных от клиента
        try:
            data = client_socket.recv(1024).decode()
            print(f'Получено от клиента: {data}')
        except:
            break

    # Закрытие соединения с клиентом
    client_socket.close()

    # Закрытие серверного сокета
    server_socket.close()


if __name__ == "__main__":
    sync_socket_server()
