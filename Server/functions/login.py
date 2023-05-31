from passlib.hash import pbkdf2_sha256
from functions.utils.database_helpers import get_accounts_data

def login(uid: str, account_password: str):    
    accounts_data = get_accounts_data()

    for account in accounts_data:
        if account["uid"] == uid:
            if pbkdf2_sha256.verify(account_password, account["access_password_hash"]):
                return True
    
    return False
