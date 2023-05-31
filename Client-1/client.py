import socket

def option1():
    print("Option 1 selecionada")

def option2():
    print("Option 2 selecionada")

def option3():
    print("Option 3 selecionada")

def option4():
    print("Goodbye! See you later!")

menu = {
    1: option1,
    2: option2,
    3: option3
}

client_socket = socket.socket()

host = socket.gethostname()

port = 12345

client_socket.connect((host, port))

uid = input("Enter your account uid -> ")
password = input("Enter your password -> ")
client_socket.send(uid.encode())
client_socket.send(password.encode())

# Recebe a resposta do servidor
data = client_socket.recv(1024)

print(data.decode())

if "Hello" in data.decode():
    while True:
        print("Menu:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Exit")
        
        choice = int(input("Choose the option that indicates what you want to do -> "))
        
        if choice == 4:
            option4()
            break
        
        # Chama a função correspondente à opção escolhida
        menu[choice]()

# Fecha a conexão com o servidor
client_socket.close()
