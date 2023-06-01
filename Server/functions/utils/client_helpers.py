from functions.login import login
from functions.sign_in import sign_in , get_access_password
from functions.utils.account_helpers import get_account_by_uid

def handle_client(client_socket):
    data = client_socket.recv(1024).decode()
    
    if data == "login:1":
        name = client_socket.recv(1024).decode()
        phone = client_socket.recv(1024).decode()
        card_password = int(client_socket.recv(1024).decode())
        
        access_password = get_access_password(client_socket)
        
        if access_password is not None:
            sign_in(name, phone, access_password, card_password)

            client_socket.send("Sign in successful!".encode())
        
    elif data == "login:2":
        uid = client_socket.recv(1024).decode()
        password = client_socket.recv(1024).decode()
        
        if login(uid, password):
            account = get_account_by_uid(uid)
            
            client_socket.send(f"Hello {account['name']}! \nBalance: {account['balance']}".encode())
            
            while True:
                data = client_socket.recv(1024).decode()
                
                if data == "main:1":
                    client_socket.send("Main menu option 1 executed!".encode())
                    
                elif data == "main:2":
                    client_socket.send("Main menu option 2 executed!".encode())
                    
                elif data == "main:3":
                    client_socket.send("Main menu option 3 executed!".encode())
                    
                elif data == "main:4":
                    return "Exit"
                
    else:
        client_socket.send("Login failed!".encode())