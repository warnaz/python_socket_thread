import socket
import threading
import sys

host = input("Host: ")
port = int(input("Port: "))

try:
    # Подключаемся к серверу
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print(f"[CLIENT] Listening on {host}: {port}")
except:
    print("Невозможно подключиться к серверу. Проверьте правильность указания хоста и порта")
    input("Press enter to quit")
    sys.exit(0)

while True:
    # Клиент отправляет сообщение
    message = input("Введите сообщение: ")
    sock.sendall(str.encode(message))