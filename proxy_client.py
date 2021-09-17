from proxy_server import BUFFER_SIZE
import socket

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"


def connect(addr):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)
        # receive data from proxy
        full_data = s.recv(BUFFER_SIZE)
        print(full_data)


def main():
    connect((HOST, PORT))

if __name__ == '__main__':
    main()
