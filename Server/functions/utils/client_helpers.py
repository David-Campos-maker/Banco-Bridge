import socket
import time
from functions.login import login
from functions.sign_in import sign_in , get_access_password
from functions.utils.account_helpers import get_account_by_uid

# Global variables to store failed login attempts information
last_login_attempt_time = 0
failed_login_attempts = 0

def handle_main_menu(client_socket: socket.socket):
    while True:
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

def handle_client(client_socket: socket.socket):
    global last_login_attempt_time
    global failed_login_attempts
    
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
                sign_in(name, phone, access_password, int(card_password))
                client_socket.send("Sign in successful".encode())
                
        elif message == "login:2":
            # Check if login should be blocked
            current_time = time.time()
            if failed_login_attempts >= 3 and current_time - last_login_attempt_time < 60:
                client_socket.send("Too many failed login attempts. Please wait 1 minute before trying again.".encode())
                continue
            
            # Handle login
            uid = client_socket.recv(1024).decode()
            password = client_socket.recv(1024).decode()
            
            if login(uid, password):
                account = get_account_by_uid(uid)
                
                if account is not None:
                    client_socket.send(f"Hello {account['name']}! \nBalance: {account['balance']}".encode())
                    handle_main_menu(client_socket)
                    
                    # Reset failed login attempts
                    failed_login_attempts = 0
                else:
                    client_socket.send("Account not found!".encode())
                    
                    # Increment failed login attempts
                    failed_login_attempts += 1
                    
                    # Update last login attempt time
                    last_login_attempt_time = current_time
                    
            else:
                client_socket.send("Login failed".encode())
                
                # Increment failed login attempts
                failed_login_attempts += 1
                
                # Update last login attempt time
                last_login_attempt_time = current_time

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    client_socket, client_address = server_socket.accept()
    
    try:
        print('connection from', client_address)
        
        # Send welcome message
        welcome_message = "Welcome! Enter 1 for login or 2 for sign in"
        client_socket.send(welcome_message.encode())
        
        # Handle client connection
        handle_client(client_socket)
        
    finally:
        # Clean up the connection
        client_socket.close()
