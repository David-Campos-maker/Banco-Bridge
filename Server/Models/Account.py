import json
import os
from random import choice
from string import ascii_letters, digits
from functions.utils.account_helpers import get_account_by_uid
from passlib.hash import pbkdf2_sha256

with open(os.path.join(os.path.dirname(__file__) , ".." , "Data/currency_map.json") , "r") as currency_map_file:
    currency_map = json.load(currency_map_file)

class Account:
    def __init__(self , name: str , phone: str , access_password: str , card_password: int):
        self.name =  name
        self.uid = self.generate_uid()
        self.balance = 0.00
        self.phone = phone
        
        international_area_code = phone.split('-')[0]
        self.currency = currency_map.get(international_area_code , "USD")
        
        self.access_password = pbkdf2_sha256.hash(access_password)
        self.card_password = pbkdf2_sha256.hash(str(card_password))
        
    def generate_uid(self):
        letters = "".join(choice(ascii_letters) for _ in range(4))
        numbers = "".join(choice(digits) for _ in range(4))
        uid = letters + numbers

        while get_account_by_uid(uid) is not None:
            letters = "".join(choice(ascii_letters) for _ in range(4))
            numbers = "".join(choice(digits) for _ in range(4))
            uid = letters + numbers
            
        return uid
    