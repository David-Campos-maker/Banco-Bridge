import socket
from helpers.menu_functions import login_or_sign_in_menu

client_socket = socket.socket()

host = socket.gethostname()

port = 12345

client_socket.connect((host, port))

login_or_sign_in_menu(client_socket)

client_socket.close()










# uid = input("Enter your account uid -> ")
# password = input("Enter your password -> ")
# client_socket.send(uid.encode())
# client_socket.send(password.encode())

# # Recebe a resposta do servidor
# data = client_socket.recv(1024)

# print(data.decode())

# if "Hello" in data.decode():
#     while True:
#         print("Menu:")
#         print("1. Option 1")
#         print("2. Option 2")
#         print("3. Option 3")
#         print("4. Exit")
        
#         choice = int(input("Choose the option that indicates what you want to do -> "))
        
#         if choice == 4:
#             break