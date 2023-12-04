import socket
import time
import main

time.sleep(1)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((main.HOST, main.PORT))
    while True:
        inp = input("Input: ")
        s.sendall(inp.encode())
        if inp == "!close":
            break
        while True:
            data = s.recv(1024)
            if not data:
                break
            byte_text = bytearray()
            for b in data:
                if b == 0x03:
                    break
                byte_text.append(b)
                #print(chr(b), end="")
            else:
                print(byte_text.decode(),end="")
                continue
            print(byte_text.decode(),end="")
            break