from functions.utils.database_helpers import add_new_user
    
def sign_in(name: str , phone: str , access_password: str , card_password: int):
    add_new_user(name , phone , access_password , card_password)

def get_access_password(client_socket):
    while True:
        client_socket.send("Enter access password".encode())
        
        access_password = client_socket.recv(1024).decode()
        
        if is_valid_password(access_password):
            return access_password

def is_valid_password(access_password):
    return all([
        len(access_password) >= 8 ,
        len(access_password) <= 14,
        any(char.isdigit() for char in access_password) ,
        any(char.isupper() for char in access_password) ,
        any(char in "!@#$%^&*()" for char in access_password) ,
    ])
