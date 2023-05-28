import json 

def transfer(creditors_uid , debtors_uid):
    with open("../database.json" , "r") as data_base_file:
        data_base = json.load(data_base_file)
        accounts_data = data_base["accounst"]
        
    creditors_data = {} 
    debtors_data = {}
       
    for account in accounts_data:
        if account["uid"] == creditors_uid:
            creditors_data == account