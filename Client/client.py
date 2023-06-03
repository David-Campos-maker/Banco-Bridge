import socket
from helpers.menu_functions import login_or_sign_in_menu

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Receive welcome message from server
    welcome_message = client_socket.recv(1024).decode()
    print(welcome_message)
    
    # Show login or sign in menu
    login_or_sign_in_menu(client_socket)
    
finally:
    # Clean up the connection
    client_socket.close()
