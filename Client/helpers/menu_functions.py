import socket
import json

def main_menu(client_socket: socket.socket):
    print("\n******************")
    print("**  Main Menu   **")
    print("******************\n")
    
    print("1. Transfer")
    print("2. Transfer with savings account")
    print("3. Deposit into savings account")
    print("4. Transfer with credit")
    print("5. Pay credit invoice with savings account")
    print("6. Pay credit invoice")
    print("7. View statement")
    print("8. Logout")

    choice = input("Choose the option that indicates what you want to do -> ")

    if choice not in ["1", "2", "3", "4" , "5" , "6" , "7", "8"]:
        print("Invalid choice!")
        main_menu(client_socket)
        return
    
    if choice == "1":
        debtors_uid = input("Enter your uid -> ")
        creditors_uid = input("Enter the target uid -> ")
        transfer_amount = float(input("Enter the transfer amount -> "))
        card_password = int(input("Enter your card password -> "))
        
        transfer_data = ",".join([debtors_uid , creditors_uid , str(transfer_amount) , str(card_password)])
        
        client_socket.send("main:1".encode())
        
        trigger_message = client_socket.recv(1024).decode()
        print(trigger_message)
        
        client_socket.send(transfer_data.encode())
        
        return_message = client_socket.recv(1024).decode()
        print(return_message)
        
    if choice == "2":
        debtors_uid = input("Enter your uid -> ")
        creditors_uid = input("Enter the target uid -> ")
        transfer_amount = float(input("Enter the transfer amount -> "))
        card_password = int(input("Enter your card password -> "))
        
        transfer_data = ",".join([debtors_uid , creditors_uid , str(transfer_amount) , str(card_password)])
        
        client_socket.send("main:2".encode())
        
        trigger_message = client_socket.recv(1024).decode()
        print(trigger_message)
        
        client_socket.send(transfer_data.encode())
        
        return_message = client_socket.recv(1024).decode()
        print(return_message)
        
    if choice == "3":
        debtors_uid = input("Enter your uid -> ")
        transfer_amount = float(input("Enter the transfer amount -> "))
        card_password = int(input("Enter your card password -> "))
        
        transfer_data = ",".join([debtors_uid , str(transfer_amount) , str(card_password)])
        
        client_socket.send("main:3".encode())
        
        trigger_message = client_socket.recv(1024).decode()
        print(trigger_message)
        
        client_socket.send(transfer_data.encode())
        
        return_message = client_socket.recv(1024).decode()
        print(return_message)
        
    if choice == "4":
        debtors_uid = input("Enter your uid -> ")
        creditors_uid = input("Enter the target uid -> ")
        transfer_amount = float(input("Enter the transfer amount -> "))
        card_password = int(input("Enter your card password -> "))
        
        transfer_data = ",".join([debtors_uid , creditors_uid , str(transfer_amount) , str(card_password)])
        
        client_socket.send("main:4".encode())
        
        trigger_message = client_socket.recv(1024).decode()
        print(trigger_message)
        
        client_socket.send(transfer_data.encode())
        
        return_message = client_socket.recv(1024).decode()
        print(return_message)
        
    if choice == "5":
        user_uid = input("Enter your uid -> ")
        card_password = int(input("Enter your card password -> "))
        
        transfer_data = ",".join([user_uid , str(card_password)])
        
        client_socket.send("main:5".encode())
        
        trigger_message = client_socket.recv(1024).decode()
        print(trigger_message)
        
        client_socket.send(transfer_data.encode())
        
        return_message = client_socket.recv(1024).decode()
        print(return_message)
        
    if choice == "6":
        user_uid = input("Enter your uid -> ")
        card_password = int(input("Enter your card password -> "))
        
        transfer_data = ",".join([user_uid , str(card_password)])
        
        client_socket.send("main:6".encode())
        
        trigger_message = client_socket.recv(1024).decode()
        print(trigger_message)
        
        client_socket.send(transfer_data.encode())
        
        return_message = client_socket.recv(1024).decode()
        print(return_message)

    if choice == "7":
      # Option to view statement
      uid = input("Enter your uid -> ")
      
      client_socket.send("main:7".encode())
      client_socket.send(uid.encode())
      
      statement_str = client_socket.recv(1024).decode()
      statement = json.loads(statement_str)
      
      for transaction in statement:
          print(f"{transaction['date']}: {transaction['amount']} to/from: {transaction['destination']}")

    if choice == "8":
      client_socket.send("main:8".encode())
      return

    main_menu(client_socket)
    
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
