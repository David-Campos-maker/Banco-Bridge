import json
import os
from typing import Optional

DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..' ,'..', 'Data/database.json')

def get_account_by_uid(desired_uid: str) -> Optional[dict]:
    with open(DATABASE_PATH , "r") as data_base_file:
        data_base = json.load(data_base_file)
        accounts_data = data_base["accounts"]
        
    for account in accounts_data:
        if account["uid"] == desired_uid:
            return account
        
    print("Uid not registered!")
    return None
        