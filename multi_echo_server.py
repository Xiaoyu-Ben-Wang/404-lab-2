import socket
from multiprocessing import Process

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024


def handle_request(addr, conn):
    ext_data = conn.recv(BUFFER_SIZE)
    conn.sendall(ext_data)
    conn.close()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(2)

        while True:
            conn, addr = server.accept()
            p = Process(target=handle_request, args=(addr, conn))
            p.daemon = True
            p.start()


if __name__ == '__main__':
    main()
