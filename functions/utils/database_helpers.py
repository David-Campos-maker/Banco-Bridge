import json
import os
from random import randrange

DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..' ,'..', 'database.json')

def get_accounts_data(): 
    with open(DATABASE_PATH , "r") as data_base_file:
        data_base = json.load(data_base_file)
        accounts_data = data_base['accounts']
    
    return accounts_data
    
def add_new_user(name: str , phone: str , balance: float):
    uid: int = randrange(100000 ,1000000000)
    
    with open(DATABASE_PATH, "r") as data_base_file:
        data_base = json.load(data_base_file)

    if not any(account['uid'] == uid for account in data_base['accounts']):
        accounts = data_base['accounts']
        new_user = {'name' : name , 'uid' : uid , 'balance' : balance , 'phone' : phone}
        accounts.append(new_user)
        
        with open(DATABASE_PATH, "w") as data_base_file:
            json.dump(data_base , data_base_file , indent = 4)
            
    else:
        print("uid already in use! Try again")