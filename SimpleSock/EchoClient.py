import socket

HOST = "127.0.0.1"
PORT = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = ""
    while data != '-1':
        g = input("What would you like to echo? ('-1' will terminate) ")
        s.send(f'{g}'.encode())
        data = s.recv(1024).decode()
        print(f"{data}")

