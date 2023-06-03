import socket
from functions.utils.client_helpers import handle_client

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

running: bool = True

while running:
    # Wait for a connection
    print('waiting for a connection')
    client_socket, client_address = server_socket.accept()
    
    try:
        print('connection from', client_address)
        
        # Send welcome message
        welcome_message = "Welcome! Enter 1 for login or 2 for sign in"
        client_socket.send(welcome_message.encode())
        
        # Handle client connection
        result = handle_client(client_socket)
        
        if result == "Exit":
            running = False
        
    finally:
        # Clean up the connection
        client_socket.close()
