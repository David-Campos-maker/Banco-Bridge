import socket
from helpers.menu_functions import login_or_sign_in_menu

client_socket = socket.socket()

host = 'localhost'
port = 12345

client_socket.connect((host, port))

login_or_sign_in_menu(client_socket)

client_socket.close()
