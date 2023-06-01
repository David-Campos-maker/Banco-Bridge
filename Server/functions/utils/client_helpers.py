from functions.login import login
from functions.sign_in import sign_in
from functions.utils.account_helpers import get_account_by_uid

def handle_client(client_socket):
    data = client_socket.recv(1024).decode()
    
    if data == "login:1":
        client_socket.send("Sign in option executed!".encode())
        # Código para lidar com a opção 1 no menu de login (registro)
        
    elif data == "login:2":
        uid = client_socket.recv(1024).decode()
        password = client_socket.recv(1024).decode()
        
        if login(uid, password):
            account = get_account_by_uid(uid)
            
            # Envia a mensagem de sucesso e o saldo para o cliente
            client_socket.send(f"Hello {account['name']}! \nBalance: {account['balance']}".encode())
            
            while True:
                # Recebe a opção escolhida pelo cliente
                data = client_socket.recv(1024).decode()
                
                if data == "main:1":
                    # Código para executar a funcionalidade correspondente à opção 1 no menu principal
                    client_socket.send("Main menu option 1 executed!".encode())
                elif data == "main:2":
                    # Código para executar a funcionalidade correspondente à opção 2 no menu principal
                    client_socket.send("Main menu option 2 executed!".encode())
                elif data == "main:3":
                    # Código para executar a funcionalidade correspondente à opção 3 no menu principal
                    client_socket.send("Main menu option 3 executed!".encode())
                elif data == "main:4":
                    # Retorna um valor para indicar que o usuário escolheu sair da aplicação
                    return "Exit"
    else:
        client_socket.send("Login failed!".encode())