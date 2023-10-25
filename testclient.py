import socket
import main

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((main.HOST, main.PORT))
    while True:
        s.sendall(input().encode())
        data = s.recv(1024)

        print(f"Received {data}")