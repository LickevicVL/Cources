import socket
from threading import Thread

sock = socket.socket()
sock.bind((socket.gethostname(), 5555))
sock.listen()


def connector(conn, addr):
    print('Connect from: ', addr)
    while True:
        name = conn.recv(1024).decode()
        if not name:
            conn.close()

            break

        conn.send(f'Hi {name}'.encode())


if __name__ == '__main__':
    while True:
        conn, addr = sock.accept()
        thread = Thread(target=connector, args=(conn, addr))
        thread.start()
