import json
import os
import sys
sys.path.insert(1 , "./database_helpers.py")
from database_helpers import get_accounts_data

DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..' ,'..', 'database.json')

def get_account_by_uid(desired_uid: int):
    accounts_data = get_accounts_data()
        
    for account in accounts_data:
        if account["uid"] == desired_uid:
            return account
        
    print("Uid not registered!")
    return None
        