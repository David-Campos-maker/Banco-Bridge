import json
import os
from random import randrange

DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..' ,'..', 'database.json')

def get_database():
    with open(DATABASE_PATH , "r") as data_base_file:
        return json.load(data_base_file)

def get_accounts_data(): 
    data_base = get_database()
    return data_base['accounts']
    
def add_new_user(name: str , phone: str , balance: float):
    uid: int = randrange(100000 ,1000000000)
    
    data_base = get_database()

    if not any(account['uid'] == uid for account in data_base['accounts']):
        accounts = data_base['accounts']
        new_user = {'name' : name , 'uid' : uid , 'balance' : balance , 'phone' : phone}
        accounts.append(new_user)
        
        with open(DATABASE_PATH, "w") as data_base_file:
            json.dump(data_base , data_base_file , indent = 4)
            
    else:
        print("uid already in use! Try again")
        
def updade_account_data(uid: int , new_data: dict):
    data_base = get_database()
    
    account_found: bool = False
    
    for account in data_base['accounts']:
        if account['uid'] == uid:
            account.update(new_data)
            account_found = True
            break
        
    if not account_found:
        print(f"Account with uid {uid} not found!")
        return
    
    try:
        with open(DATABASE_PATH , "w") as data_base_file:
            json.dump(data_base , data_base_file , indent = 4)
            
    except Exception as error:
        print(f"An error occurred while updating the database: {error}")
        
def update_account_balance(uid: int, new_balance: float):
    data_base = get_database()
    
    account_found: bool = False
    
    for account in data_base['accounts']:
        if account['uid'] == uid:
            account['balance'] = new_balance
            account_found = True
            break
    
    if not account_found:
        print(f"Account with uid {uid} not found!")
        return
    
    try:
        with open(DATABASE_PATH , "w") as data_base_file:
            json.dump(data_base , data_base_file , indent = 4)
            
    except Exception as error:
        print(f"An error occurred while updating the database: {error}")