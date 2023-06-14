import json
import os
from Models.Account import Account

DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..' ,'..', 'Data/database.json')

def get_database():
    with open(DATABASE_PATH , "r") as data_base_file:
        return json.load(data_base_file)

def get_accounts_data(): 
    data_base = get_database()
    return data_base['accounts']
    
def add_new_user(name: str , phone: str , access_password: str , card_password: int) -> str:
    data_base = get_database()
    accounts = get_accounts_data()
    
    new_account = Account(name , phone , access_password , card_password)
    
    new_user: dict = {
        'name' : new_account.name , 
        'uid' : new_account.uid , 
        'balance' : new_account.balance , 
        'phone' : new_account.phone , 
        'currency': new_account.currency ,
        'access_password_hash': new_account.access_password ,
        'card_password_hash': new_account.card_password ,
        'credit_card': {
            'approved_limit': new_account.credit_card.approved_limit ,
            'invoice': new_account.credit_card.invoice ,
            'changed_limit': new_account.credit_card.changed_limit
        },
        'savings': new_account.savings
    }
    
    accounts.append(new_user)
    
    data_base['accounts'] = accounts
    
    try:
        with open(DATABASE_PATH, "w") as data_base_file:
            json.dump(data_base , data_base_file , indent = 4)
            
        print("Account created successfully")
        return f"Your account id is: '{new_account.uid}'. It will be with it that you will access your account and transfer, together with your passwords. Don't miss it!"
            
    except Exception as error:
        print(f"An error occurred while adding new user: {error}")
        return f"An error occurred while adding new user: {error}"
        
        
def updade_account_data(uid: str , new_data: dict):
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
        
def update_account_balance(uid: str, new_balance: float):
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
        
def update_account_savings(uid: str, new_savings: float):
    data_base = get_database()
    
    account_found: bool = False
    
    for account in data_base['accounts']:
        if account['uid'] == uid:
            account['savings'] = new_savings
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
        
def update_credit_invoice(uid:str , new_invoice: float):
    data_base = get_database()
    
    account_found: bool = False
    
    for account in data_base["accounts"]:
        if account["uid"] == uid:
            account["credit_card"]["invoice"] = new_invoice
            account_found = True
            break
        
    if not account_found:
        print(f"Account with uid {uid} not found!")
        
    try:
        with open(DATABASE_PATH , "w") as data_base_file:
            json.dump(data_base , data_base_file , indent = 4)
    
    except Exception as error:
        print(f"An error occurred while updating the database: {error}")
        
def update_account_statement(uid: str, new_statement):
    data_base = get_database()
    
    account_found: bool = False
    
    for account in data_base['accounts']:
        if account['uid'] == uid:
            account['statement'] = new_statement
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
