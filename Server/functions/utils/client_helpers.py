import socket
from functions.login import login
from functions.transactions import *
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
        
        debtors_uid , creditors_uid , transfer_amount , card_password = tranfer_data.split(",")
        result = transfer(debtors_uid , creditors_uid , float(transfer_amount) , card_password)
        
        client_socket.send(result.encode())
        
        print("Transação Feita")
            
    elif message == "main:2":
        # Handle option 2
        client_socket.send("Transfer with savings account executed".encode())
        
        tranfer_data = client_socket.recv(1024).decode()
        
        debtors_uid , creditors_uid , transfer_amount , card_password = tranfer_data.split(",")
        result = transfer_with_savings_account(debtors_uid , creditors_uid , float(transfer_amount) , card_password)
        
        client_socket.send(result.encode())
        
        print("Transação Feita")
        
    elif message == "main:3":
        # Handle option 3
        client_socket.send("Deposit into savings account executed".encode())
        
        tranfer_data = client_socket.recv(1024).decode()
        
        debtors_uid , transfer_amount , card_password = tranfer_data.split(",")
        result = deposit_into_savings_account(debtors_uid , float(transfer_amount) , card_password)
        
        client_socket.send(result.encode())
        
        print("Transação Feita")
        
    elif message == "main:4":
        # Handle option 4
        client_socket.send("Transfer with credit".encode())
        
        tranfer_data = client_socket.recv(1024).decode()
        
        debtors_uid , creditors_uid , transfer_amount , card_password = tranfer_data.split(",")
        result = transfer_with_credit(debtors_uid , creditors_uid , float(transfer_amount) , card_password)
        
        client_socket.send(result.encode())
        
        print("Transação Feita")
        
    elif message == "main:5":
        # Handle option 5
        client_socket.send("Pay credit invoice".encode())
        
        tranfer_data = client_socket.recv(1024).decode()
        
        user_uid , card_password = tranfer_data.split(",")
        
        result = pay_credit_invoice_with_savings_account(user_uid , card_password)
        
        client_socket.send(result.encode())
        
        print("Transação Feita")
        
    elif message == "main:6":
        # Handle option 6
        client_socket.send("Pay credit invoice".encode())
        
        tranfer_data = client_socket.recv(1024).decode()
        
        user_uid , card_password = tranfer_data.split(",")
        
        result = pay_credit_invoice(user_uid , card_password)
        
        client_socket.send(result.encode())
        
        print("Transação Feita")
        
    elif message == "main:7":
        # Handle logout
        return True
    
    handle_main_menu(client_socket)
    return False

def handle_client(client_socket: socket.socket):
    while True:
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
                    client_socket.send(
                        f"Hello {account['name']}! \nBalance: {account['balance']}\nCredit Limit: {account['credit_card']['changed_limit']}\t Credit invoice: {account['credit_card']['invoice']}\n".encode()
                        )
                    
                    logged_out = handle_main_menu(client_socket)
                    if logged_out:
                        break
                else:
                    client_socket.send("Account not found!".encode())    
                    
            else:
                client_socket.send("Login failed".encode())
                
        elif message == "login:3":
            client_socket.send("Goodbye!".encode())
            break
