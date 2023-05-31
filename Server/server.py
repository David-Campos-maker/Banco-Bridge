import socket
from functions.login import login
from functions.utils.account_helpers import get_account_by_uid

server_socket = socket.socket()

host = socket.gethostname()

port = 12345

server_socket.bind((host, port))

print("Waiting for connection...")
server_socket.listen(5)

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection received from {addr}")
    
    uid = client_socket.recv(1024).decode()
    password = client_socket.recv(1024).decode()
    
    if login(uid, password):
        account = get_account_by_uid(uid)
        
        # Envia a mensagem de sucesso e o saldo para o cliente
        client_socket.send(f"Hello {account['name']}! \nBalance: {account['balance']}".encode())
        
        # Aqui você pode adicionar outras funcionalidades que deseja disponibilizar ao cliente após o login bem-sucedido
    else:
        client_socket.send("Login failed!".encode())

    client_socket.close()


