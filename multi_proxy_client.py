import socket
from multiprocessing import Pool

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"


def connect(addr):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_socket:
        proxy_socket.connect(addr)
        proxy_socket.sendall(payload.encode())
        proxy_socket.shutdown(socket.SHUT_WR)

        full_data = proxy_socket.recv(BUFFER_SIZE)
        print(full_data)


def main():
    with Pool() as p:
        p.map(connect, [(HOST, PORT)]*5)


if __name__ == '__main__':
    main()
