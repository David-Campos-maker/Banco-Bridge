import socket
from functions.utils.database_helpers import add_new_user
    
def sign_in(name: str , phone: str , access_password: str , card_password: int):
    result = add_new_user(name , phone , access_password , card_password)
    
    return result

def get_access_password(client_socket: socket.socket) -> str:
    client_socket.send("Enter access password".encode())
    access_password: str = client_socket.recv(1024).decode()
    
    if is_valid_password(access_password):
        return access_password
    else:
        client_socket.send("Invalid password. Try again.".encode())
        return get_access_password(client_socket)

def is_valid_password(access_password: str):
    return all([
        len(access_password) >= 8 ,
        len(access_password) <= 14,
        any(char.isdigit() for char in access_password) ,
        any(char.isupper() for char in access_password) ,
        any(char in "!@#$%^&*()" for char in access_password) ,
    ])
