import json
from random import randrange

uid = randrange(100000 ,1000000000)
name = str(input('Your name -> '))
phone = str(input('Your phone number (Use your location code ex: +55-your number) -> '))
balance = 100.00

with open("database.json", "r") as data_base_file:
    data_base = json.load(data_base_file)

if not any(account['uid'] == uid for account in data_base['accounts']):
    accounts = data_base['accounts']
    new_user = {'name' : name , 'uid' : uid , 'balance' : balance , 'phone' : phone}
    accounts.append(new_user)
    
    with open("database.json", "w") as data_base_file:
        json.dump(data_base , data_base_file , indent = 4)
        
else:
    print("uid already in use! Try again")
