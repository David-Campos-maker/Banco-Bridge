from functions.utils.database_helpers import add_new_user

name = str(input('Your name -> '))
phone = str(input('Your phone number (Use your location code ex: +55-your number) -> '))

add_new_user(name , phone)

# database_path = os.path.join(os.path.dirname(__file__), 'database.json')

# with open(database_path, "r") as data_base_file:
#     data_base = json.load(data_base_file)

# if not any(account['uid'] == uid for account in data_base['accounts']):
#     accounts = data_base['accounts']
#     new_user = {'name' : name , 'uid' : uid , 'balance' : balance , 'phone' : phone}
#     accounts.append(new_user)
    
#     with open(database_path, "w") as data_base_file:
#         json.dump(data_base , data_base_file , indent = 4)
        
# else:
#     print("uid already in use! Try again")
