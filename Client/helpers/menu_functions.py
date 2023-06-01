def login_or_sign_in_menu(client_socket):
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
        
        client_socket.send(name.encode())
        client_socket.send(phone.encode())
        client_socket.send(card_password.encode())

        data = client_socket.recv(1024).decode()

        while data == "Enter access password":
            access_password = input('Choose an access password. It must contain 8 characters, including letters and special symbols -> ')
            client_socket.send(access_password.encode())
            
            data = client_socket.recv(1024).decode()

        print(data)
        
        if data == "Sign in successful!":
            login_or_sign_in_menu(client_socket)
        
    else:
        uid = input("Enter your account uid -> ")
        password = input("Enter your password -> ")
        
        client_socket.send("login:2".encode())
        client_socket.send(uid.encode())
        client_socket.send(password.encode())

        data = client_socket.recv(1024)

        print(data.decode())

        if "Hello" in data.decode():
            main_menu(client_socket)


def main_menu(client_socket):
    while True:
        print("******************")
        print("**     Menu     **")
        print("******************\n")
        
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Exit")
        
        choice = input("Choose the option that indicates what you want to do -> ")

        client_socket.send(f"main:{choice}".encode())
        
        if choice == "4":
            break

        data = client_socket.recv(1024)

        print(data.decode())


