import socket

def main_menu(client_socket: socket.socket):
    print("******************")
    print("**  Main Menu   **")
    print("******************\n")
    
    print("1. Transfer")
    print("2. Transfer with savings account")
    print("3. Deposit into savings account")
    print("4. Logout")

    choice = input("Choose the option that indicates what you want to do -> ")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice!")
        main_menu(client_socket)
        return
    
    if choice == "1":
        debtors_uid = input("Enter your uid -> ")
        creditors_uid = input("Enter the target uid -> ")
        transfer_amount = input("Enter the transfer amount -> ")
        
        transfer_data = ",".join([debtors_uid , creditors_uid , transfer_amount])
        
        client_socket.send("main:1".encode())
        
        trigger_message = client_socket.recv(1024).decode()
        print(trigger_message)
        
        client_socket.send(transfer_data.encode())
        
        return_message = client_socket.recv(1024).decode()
        print(return_message)
        
    if choice == "2":
        debtors_uid = input("Enter your uid -> ")
        creditors_uid = input("Enter the target uid -> ")
        transfer_amount = input("Enter the transfer amount -> ")
        
        transfer_data = ",".join([debtors_uid , creditors_uid , transfer_amount])
        
        client_socket.send("main:2".encode())
        
        trigger_message = client_socket.recv(1024).decode()
        print(trigger_message)
        
        client_socket.send(transfer_data.encode())
        
        return_message = client_socket.recv(1024).decode()
        print(return_message)
        
    if choice == "3":
        debtors_uid = input("Enter your uid -> ")
        transfer_amount = input("Enter the transfer amount -> ")
        
        transfer_data = ",".join([debtors_uid , transfer_amount])
        
        client_socket.send("main:3".encode())
        
        trigger_message = client_socket.recv(1024).decode()
        print(trigger_message)
        
        client_socket.send(transfer_data.encode())
        
        return_message = client_socket.recv(1024).decode()
        print(return_message)

    if choice == "4":
        client_socket.send("main:4".encode())
        return
    
    main_menu(client_socket)

def login_or_sign_in_menu(client_socket: socket.socket):
    print("******************")
    print("**     Menu     **")
    print("******************\n")
    
    print("1. Sign in")
    print("2. Login")
    print("3. Exit")

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
        
    elif choice == "2":
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
    
    else:
        client_socket.send("login:3".encode())
        exit_message = client_socket.recv(1024).decode()
        
        print(exit_message)
        return
    
    login_or_sign_in_menu(client_socket)
