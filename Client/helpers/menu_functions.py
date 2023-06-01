def login_or_sign_in_menu(client_socket):
    print("******************")
    print("**     Menu     **")
    print("******************\n")
    
    print("1. Sign in")
    print("2. Login")

    choice = input("Choose the option that indicates what you want to do -> ")

    if choice == "1":
        print("Sing in service running...")
        client_socket.send("login:1".encode())
        
    else:
        uid = input("Enter your account uid -> ")
        password = input("Enter your password -> ")
        client_socket.send("login:2".encode())
        client_socket.send(uid.encode())
        client_socket.send(password.encode())

        # Recebe a resposta do servidor
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
        
        # Recebe a resposta do servidor
        data = client_socket.recv(1024)
        
        # Exibe a resposta do servidor para o usuário
        print(data.decode())


