import socket

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

def main():
    # Question 6
    ext_host = "www.google.com"
    ext_port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print("Proxy server started.")
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST,PORT))
        proxy_start.listen(1)

        while True:
            conn, addr = proxy_start.accept()
            print(f"Connected by {addr}")

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                remote_ip = socket.gethostbyname(ext_host)
                proxy_end.connect((remote_ip, ext_port))
                ext_data = conn.recv(BUFFER_SIZE)

                print(f"Sending: {ext_data} to {ext_host}")
                proxy_end.sendall(ext_data)

                proxy_end.shutdown(socket.SHUT_WR)

                received_data = proxy_end.recv(BUFFER_SIZE)
                conn.send(received_data)
            conn.close()


if __name__=='__main__':
    main()