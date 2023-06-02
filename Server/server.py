import socket
from functions.utils.client_helpers import handle_client

server_socket = socket.socket()

host = 'localhost'
port = 12345

server_socket.bind((host, port))

print("Waiting for connection...")
server_socket.listen(5)

running: bool = True

while running:
    client_socket, addr = server_socket.accept()
    print(f"Connection received from {addr}")
    
    result = handle_client(client_socket)

    client_socket.close()
    
    if result == "Exit":
        print(f"Connection to the address {addr} was terminated")
        running = False
