import socket

def main_menu(client_socket: socket.socket):
    while True:
        print("******************")
        print("**  Main Menu   **")
        print("******************\n")
        
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Logout")
    
        choice = input("Choose the option that indicates what you want to do -> ")
    
        if choice == "4":
            return
    
        client_socket.send(f"main:{choice}".encode())
        
        data = client_socket.recv(1024).decode()
        print(data)

def login_or_sign_in_menu(client_socket: socket.socket):
    while True:
        print("******************")
        print("**     Menu     **")
        print("******************\n")
        
        print("1. Sign in")
        print("2. Login")
    
        choice = input("Choose the option that indicates what you want to do -> ")
    
        if choice == "1":
            client_socket.send("login:1".encode())
            name = input('Your name -> ')
            phone = input('Your phone number (Use your location code ex: +55-your number) -> ')
            card_password =  input('Choose a password for your card. It must be numeric and contain 6 digits -> ')
            
            user_info = ",".join([name, phone, card_password])
            client_socket.send(user_info.encode())
    
            data = client_socket.recv(1024).decode()
    
            while data == "Enter access password":
                access_password = input('Choose an access password. It must contain 8 characters, including letters and special symbols -> ')
                client_socket.send(access_password.encode())
                
                data = client_socket.recv(1024).decode()
    
            print(data)
            
        else:
            uid = input("Enter your account uid -> ")
            password = input("Enter your password -> ")
            
            client_socket.send("login:2".encode())
            client_socket.send(uid.encode())
            client_socket.send(password.encode())
    
            data = client_socket.recv(1024).decode()
    
            if "Hello" in data:
                print(data)
                main_menu(client_socket)
            else:
                print(data)

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
