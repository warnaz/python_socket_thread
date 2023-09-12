import socket
import threading
from utils import port

connections = []
total_connections = 0


def api_test(client_id, message):
    print("ID " + str(client_id) + ": " + message)


class Client(threading.Thread):
    def __init__(self, socket, address, id, name, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal

    def __str__(self):
        return str(self.id) + " " + str(self.address)

    def run(self):
        while self.signal:
            try:
                data = self.socket.recv(1024)
            except:
                print("Client " + str(self.address) + " has disconnected")
                self.signal = False
                connections.remove(self)
                break
            if data.decode('utf-8') in ('exit', 'break', 'quit', 'q'):
                print("Client " + str(self.address) + " has disconnected")
                self.signal = False
                connections.remove(self)
                break
            elif data:
                # Oтправляем сообщение клиента в АПИ
                msg = data.decode("utf-8")
                api_test(self.id, msg)


def newConnections(socket):
    # Подключение нового клиента
    while True:
        sock, address = socket.accept()
        global total_connections

        connections.append(Client(sock, address, total_connections, "Name", True))
        connections[len(connections) - 1].start()

        print("New connection at ID " + str(connections[len(connections) - 1]))
        total_connections += 1


def main():
    # Запуск сервера
    host = 'localhost'
    _port = port

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind((host, _port))
    sock.listen()
    print(f"[SERVER] Listening on {host}: {port}")

    newConnectionsThread = threading.Thread(target=newConnections, args=(sock,))
    newConnectionsThread.start()


if __name__ == "__main__":
    main()
