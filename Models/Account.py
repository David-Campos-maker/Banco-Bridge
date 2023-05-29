import json
import os
from random import choice
from string import ascii_letters, digits
from functions.utils.account_helpers import get_account_by_uid

with open(os.path.join(os.path.dirname(__file__) , ".." , "Data/currency_map.json") , "r") as currency_map_file:
    currency_map = json.load(currency_map_file)

class Account:
    def __init__(self , name: str , phone: str):
        self.name =  name
        self.uid = self.generate_uid()
        self.balance = 0.00
        self.phone = phone
        
        international_area_code = phone.split('-')[0]
        self.currency = currency_map.get(international_area_code , "USD")
        
    def generate_uid(self):
        letters = "".join(choice(ascii_letters) for _ in range(4))
        numbers = "".join(choice(digits) for _ in range(4))
        uid = letters + numbers

        while get_account_by_uid(uid) is not None:
            letters = "".join(choice(ascii_letters) for _ in range(4))
            numbers = "".join(choice(digits) for _ in range(4))
            uid = letters + numbers
            
        return uid
    
    