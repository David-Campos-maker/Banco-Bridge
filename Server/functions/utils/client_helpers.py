import socket
from functions.login import login
from functions.sign_in import sign_in , get_access_password
from functions.utils.account_helpers import get_account_by_uid

def handle_main_menu(client_socket: socket.socket):
    # Receive message from client
    message = client_socket.recv(1024).decode()
    
    # Handle main menu choice
    if message == "main:1":
        # Handle option 1
        client_socket.send("Option 1 executed".encode())
            
    elif message == "main:2":
        # Handle option 2
        client_socket.send("Option 2 executed".encode())
        
    elif message == "main:3":
        # Handle option 3
        client_socket.send("Option 3 executed".encode())
        
    elif message == "main:4":
        # Handle logout
        return
    
    handle_main_menu(client_socket)

def handle_client(client_socket: socket.socket):
    # Receive message from client
    message = client_socket.recv(1024).decode()
    
    # Handle login or sign in choice
    if message == "login:1":
        # Handle sign in
        user_info = client_socket.recv(1024).decode()
        name, phone, card_password = user_info.split(",")
        
        access_password = get_access_password(client_socket)
        
        if access_password is not None:
            sign_in(name, phone, access_password, int(card_password))
            client_socket.send("Sign in successful".encode())
            
    elif message == "login:2":
        # Handle login
        uid = client_socket.recv(1024).decode()
        password = client_socket.recv(1024).decode()
        
        if login(uid, password):
            account = get_account_by_uid(uid)
            
            if account is not None:
                client_socket.send(f"Hello {account['name']}! \nBalance: {account['balance']}".encode())
                handle_main_menu(client_socket)

            else:
                client_socket.send("Account not found!".encode())    
                
        else:
            client_socket.send("Login failed".encode())
            
    elif message == "login:3":
        client_socket.send("Goodbye!".encode())
        return "Exit"
    
    handle_client(client_socket)
