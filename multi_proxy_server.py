from proxy_server import BUFFER_SIZE
import socket
from multiprocessing import Process

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

def handle_request(addr, conn, proxy):
    print("Connected to:", addr)

    ext_data = conn.recv(BUFFER_SIZE) # get data from client
    proxy.sendall(ext_data) # send data to google
    recv_data = proxy.recv(BUFFER_SIZE) # receive data from google
    conn.sendall(recv_data) # pass data back to client
    proxy.shutdown(socket.SHUT_WR)



def main():
    ext_host = "www.google.com"
    ext_port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print("Proxy server started.")
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(1)

        while True:
            conn, addr = proxy_start.accept()
            print(f"Connected by {addr}")

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                remote_ip = socket.gethostbyname(ext_host)
                proxy_end.connect((remote_ip, ext_port))

                p = Process(target=handle_request, args=(addr, conn, proxy_end))
                p.start()
                print("Started new process", p)

            conn.close()

if __name__=='__main__':
    main()