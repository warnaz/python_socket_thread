import socket
from utils import port


def sync_socket_server():
    # �������� ������� ������
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # �������� ������ � ������ � �����
    server_address = ('localhost', port)
    server_socket.bind(server_address)

    # ������������� �������� ����������
    server_socket.listen()
    print('������ ������� � ������� ����������� ��������...')

    while True:
        # �������� ��������� ����������
        client_socket, client_address = server_socket.accept()
        print(f'����� ����������� �� {client_address}')

        # ��������� ������ �� �������
        try:
            data = client_socket.recv(1024).decode()
            print(f'�������� �� �������: {data}')
        except:
            break

    # �������� ���������� � ��������
    client_socket.close()

    # �������� ���������� ������
    server_socket.close()


if __name__ == "__main__":
    sync_socket_server()
