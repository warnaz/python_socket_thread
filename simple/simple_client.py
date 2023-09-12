import socket
import sys

host = input("Host: ")
port = int(input("Port: "))

try:
    # ������������ � �������
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('[CLIENT] Connecting to %s:%s' % (host, port))
except:
    print("���������� ������������ � �������. ��������� ������������ �������� ����� � �����")
    input("Press enter to quit")
    sys.exit(0)

while True:
    # ������ ���������� ���������
    message = input('������� ���������: ')
    sock.sendall(str.encode(message))
