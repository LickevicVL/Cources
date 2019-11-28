import socket

sock = socket.socket()
sock.connect((socket.gethostname(), 5555))

if __name__ == '__main__':
    name = input('Name: ')
    sock.send(name.encode())
    print(sock.recv(1024).decode())
