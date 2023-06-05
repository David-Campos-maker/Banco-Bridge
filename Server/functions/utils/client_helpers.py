import socket
from functions.login import login
from functions.transactions import transfer
from functions.sign_in import sign_in , get_access_password
from functions.utils.account_helpers import get_account_by_uid

def handle_main_menu(client_socket: socket.socket) -> bool:
    # Receive message from client
    message = client_socket.recv(1024).decode()
    
    # Handle main menu choice
    if message == "main:1":
        # Handle option 1
        client_socket.send("Transfer executed".encode())
        
        tranfer_data = client_socket.recv(1024).decode()
        
        debtors_uid , creditors_uid , transfer_amount = tranfer_data.split(",")
        result = transfer(debtors_uid , creditors_uid , float(transfer_amount))
        
        client_socket.send(result.encode())
        
        print("Transação Feita")
            
    elif message == "main:2":
        # Handle option 2
        client_socket.send("Option 2 executed".encode())
        
    elif message == "main:3":
        # Handle option 3
        client_socket.send("Option 3 executed".encode())
        
    elif message == "main:4":
        # Handle logout
        return True
    
    handle_main_menu(client_socket)
    return False

def handle_client(client_socket: socket.socket) -> str:
    # Receive message from client
    message = client_socket.recv(1024).decode()
    
    # Handle login or sign in choice
    if message == "login:1":
        # Handle sign in
        user_info = client_socket.recv(1024).decode()
        name, phone, card_password = user_info.split(",")
        
        access_password = get_access_password(client_socket)
        
        if access_password is not None:
            result_message = sign_in(name, phone, access_password, int(card_password))
            client_socket.send(result_message.encode())
            
    elif message == "login:2":
        # Handle login
        uid = client_socket.recv(1024).decode()
        password = client_socket.recv(1024).decode()
        
        if login(uid, password):
            account = get_account_by_uid(uid)
            
            if account is not None:
                client_socket.send(f"Hello {account['name']}! \nBalance: {account['balance']}".encode())
                logged_out = handle_main_menu(client_socket)
                if logged_out:
                    handle_client(client_socket)
            else:
                client_socket.send("Account not found!".encode())    
                
        else:
            client_socket.send("Login failed".encode())
            
    elif message == "login:3":
        client_socket.send("Goodbye!".encode())
        client_socket.close()
        return "Exit"
    
    handle_client(client_socket)
