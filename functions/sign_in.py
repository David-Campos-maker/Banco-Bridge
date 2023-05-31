from functions.utils.database_helpers import add_new_user
    
def sign_in():
    name = str(input('Your name -> '))
    phone = str(input('Your phone number (Use your location code ex: +55-your number) -> '))
    access_password = get_access_password()
    card_password =  int(input('Choose a password for your card. It must be numeric and contain 6 digits -> '))

    add_new_user(name , phone , access_password , card_password)

def get_access_password():
    access_password = str(input('Choose an access password. It must contain 8 characters, including letters and special symbols -> '))
    
    if is_valid_password(access_password):
        return access_password

    print("Invalid password. Please try again.")
    return get_access_password()

def is_valid_password(access_password):
    return all([
        len(access_password) == 8 ,
        any(char.isdigit() for char in access_password) ,
        any(char.isupper() for char in access_password) ,
        any(char in "!@#$%^&*()" for char in access_password) ,
    ])
