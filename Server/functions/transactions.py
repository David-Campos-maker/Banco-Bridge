from datetime import datetime
from functions.utils.account_helpers import get_account_by_uid
from functions.utils.database_helpers import update_account_balance , update_account_savings , update_credit_invoice , update_account_statement
from Exchange.exchange_api import get_currency_rate_by_code
from passlib.hash import pbkdf2_sha256

def transfer(debtors_uid: str , creditors_uid: str , transfer_amount: float , card_password: str) -> str:
    try:
        DEBTORS_ACCOUNT_DATA = get_account_by_uid(debtors_uid)
        if DEBTORS_ACCOUNT_DATA is None:
            raise ValueError(f"Error: account with uid {debtors_uid} not found")
        
        CREDITORS_ACCOUNT_DATA = get_account_by_uid(creditors_uid)
        if CREDITORS_ACCOUNT_DATA is None:
            raise ValueError(f"Error: account with uid {creditors_uid} not found")
        
        # Check if the "statement" object exists and create it if it does not exist
        if "statement" not in DEBTORS_ACCOUNT_DATA:
            DEBTORS_ACCOUNT_DATA["statement"] = []
        if "statement" not in CREDITORS_ACCOUNT_DATA:
            CREDITORS_ACCOUNT_DATA["statement"] = []
        
        DEBTORS_CURRENCY_RATES = get_currency_rate_by_code(DEBTORS_ACCOUNT_DATA["currency"])
        if DEBTORS_CURRENCY_RATES is None:
            raise ValueError(f"Error: currency rate for {DEBTORS_ACCOUNT_DATA['currency']} not found")
        
        amount_to_be_debited = transfer_amount * DEBTORS_CURRENCY_RATES[CREDITORS_ACCOUNT_DATA["currency"]] * 0.0425
        
        # Check the card password before proceeding with the transaction
        if pbkdf2_sha256.verify(card_password , DEBTORS_ACCOUNT_DATA["card_password_hash"]):
            if DEBTORS_ACCOUNT_DATA["balance"] >= amount_to_be_debited:
                CREDITORS_ACCOUNT_DATA["balance"] += transfer_amount
                DEBTORS_ACCOUNT_DATA["balance"] -= amount_to_be_debited
                
                # Add the transaction to the statement list of each user
                current_date = datetime.now().strftime("%Y-%m-%d")
                DEBTORS_ACCOUNT_DATA["statement"].append({
                    "destination": creditors_uid,
                    "amount": -amount_to_be_debited,
                    "date": current_date
                })
                CREDITORS_ACCOUNT_DATA["statement"].append({
                    "destination": debtors_uid,
                    "amount": transfer_amount,
                    "date": current_date
                })
                
                update_account_balance(creditors_uid , CREDITORS_ACCOUNT_DATA["balance"])
                update_account_balance(debtors_uid , DEBTORS_ACCOUNT_DATA["balance"])
                
                update_account_statement(debtors_uid, DEBTORS_ACCOUNT_DATA["statement"])
                update_account_statement(creditors_uid, CREDITORS_ACCOUNT_DATA["statement"])
                
                return "Transaction successful!"
            
            else:
                CREDITORS_ACCOUNT_DATA["balance"] += transfer_amount
                DEBTORS_ACCOUNT_DATA["balance"] -= amount_to_be_debited * 0.1
                
                update_account_balance(creditors_uid , CREDITORS_ACCOUNT_DATA["balance"])
                update_account_balance(debtors_uid , DEBTORS_ACCOUNT_DATA["balance"])
                
                return "Insufficient funds! The transfer was completed generating a debt of 10%" 
        
        else:
            return "Incorrect card password!"
        
    except Exception as error:
        return f"An error occurred! {error}"

def transfer_with_savings_account(debtors_uid: str , creditors_uid: str , transfer_amount: float , card_password: str) -> str:
    try:
        DEBTORS_ACCOUNT_DATA = get_account_by_uid(debtors_uid)
        if DEBTORS_ACCOUNT_DATA is None:
            raise ValueError(f"Error: account with uid {debtors_uid} not found")
        
        CREDITORS_ACCOUNT_DATA = get_account_by_uid(creditors_uid)
        if CREDITORS_ACCOUNT_DATA is None:
            raise ValueError(f"Error: account with uid {creditors_uid} not found")
        
        # Check if the "statement" object exists and create it if it does not exist
        if "statement" not in DEBTORS_ACCOUNT_DATA:
            DEBTORS_ACCOUNT_DATA["statement"] = []
        if "statement" not in CREDITORS_ACCOUNT_DATA:
            CREDITORS_ACCOUNT_DATA["statement"] = []
        
        DEBTORS_CURRENCY_RATES = get_currency_rate_by_code(DEBTORS_ACCOUNT_DATA["currency"])
        if DEBTORS_CURRENCY_RATES is None:
            raise ValueError(f"Error: currency rate for {DEBTORS_ACCOUNT_DATA['currency']} not found")
        
        amount_to_be_debited = transfer_amount * DEBTORS_CURRENCY_RATES[CREDITORS_ACCOUNT_DATA["currency"]] * 0.0425
        
        # Check the card password before proceeding with the transaction
        if pbkdf2_sha256.verify(card_password , DEBTORS_ACCOUNT_DATA["card_password_hash"]):
            if DEBTORS_ACCOUNT_DATA["savings"] >= amount_to_be_debited:
                CREDITORS_ACCOUNT_DATA["balance"] += transfer_amount
                DEBTORS_ACCOUNT_DATA["savings"] -= amount_to_be_debited
                
                # Add the transaction to the statement list of each user
                current_date = datetime.now().strftime("%Y-%m-%d")
                DEBTORS_ACCOUNT_DATA["statement"].append({
                    "destination": creditors_uid,
                    "amount": -amount_to_be_debited,
                    "date": current_date
                })
                CREDITORS_ACCOUNT_DATA["statement"].append({
                    "destination": debtors_uid,
                    "amount": transfer_amount,
                    "date": current_date
                })
                
                update_account_balance(creditors_uid , CREDITORS_ACCOUNT_DATA["balance"])
                update_account_savings(debtors_uid , DEBTORS_ACCOUNT_DATA["savings"])
                
                return "Transaction successful!"
            
            else:
                CREDITORS_ACCOUNT_DATA["balance"] += transfer_amount
                DEBTORS_ACCOUNT_DATA["savings"] -= amount_to_be_debited * 0.1
                
                update_account_balance(creditors_uid , CREDITORS_ACCOUNT_DATA["balance"])
                update_account_savings(debtors_uid , DEBTORS_ACCOUNT_DATA["savings"])
                
                return "Insufficient funds! The transfer was completed generating a debt of 10%" 
        
        else:
            return "Incorrect card password!"
        
    except Exception as error:
        return f"An error occurred! {error}"

    
def deposit_into_savings_account(user_uid: str , deposit_amount: float , card_password: str) -> str:
    try:
        USER_ACCOUNT_DATA = get_account_by_uid(user_uid)
        
        if USER_ACCOUNT_DATA is None:
            raise ValueError(f"Error: account with uid {user_uid} not found")
        
        if not pbkdf2_sha256.verify(card_password , USER_ACCOUNT_DATA["card_password_hash"]):
            return "Incorrect card password!"
        
        if USER_ACCOUNT_DATA["balance"] >= deposit_amount:
            USER_ACCOUNT_DATA["savings"] += deposit_amount
            USER_ACCOUNT_DATA["balance"] -= deposit_amount
            
            update_account_balance(user_uid , USER_ACCOUNT_DATA["balance"])
            update_account_savings(user_uid , USER_ACCOUNT_DATA["savings"])
            
            return "Transaction successful!"
        
        else:
            return "Insufficient funds!"
        
    except Exception as error:
        return f"An error occurred! {error}"
    
def transfer_with_credit(debtors_uid: str , creditors_uid: str , transfer_amount: float , card_password: str) -> str:
    try:
        DEBTORS_ACCOUNT_DATA = get_account_by_uid(debtors_uid)
        CREDITORS_ACCOUNT_DATA = get_account_by_uid(creditors_uid)
        
        if DEBTORS_ACCOUNT_DATA is None:
            raise ValueError(f"Error: account with uid {debtors_uid} not found")
        
        if CREDITORS_ACCOUNT_DATA is None:
            raise ValueError(f"Error: account with uid {creditors_uid} not found")
        
        if not pbkdf2_sha256.verify(card_password , DEBTORS_ACCOUNT_DATA["card_password_hash"]):
            return "Incorrect card password!"
        
        if DEBTORS_ACCOUNT_DATA["credit_card"]["changed_limit"] >= transfer_amount and DEBTORS_ACCOUNT_DATA["credit_card"]["invoice"] < DEBTORS_ACCOUNT_DATA["credit_card"]["changed_limit"]:
            CREDITORS_ACCOUNT_DATA["balance"] += transfer_amount
            DEBTORS_ACCOUNT_DATA["credit_card"]["invoice"] += transfer_amount
            
            update_account_balance(creditors_uid , CREDITORS_ACCOUNT_DATA["balance"])
            update_credit_invoice(debtors_uid , DEBTORS_ACCOUNT_DATA["credit_card"]["invoice"])
            
            return "Transaction successful!"
        
        else:
            return "Insufficient credit"
        
    except Exception as error:
        return f"An error occurred! {error}"
            
def pay_credit_invoice(user_uid: str , card_password: str) -> str:
    try:
        USER_ACCOUNT_DATA = get_account_by_uid(user_uid)
        
        if USER_ACCOUNT_DATA is None:
            raise ValueError(f"Error: account with uid {user_uid} not found")
        
        if not pbkdf2_sha256.verify(card_password , USER_ACCOUNT_DATA["card_password_hash"]):
            return "Incorrect card password!"
        
        if USER_ACCOUNT_DATA["balance"] >= USER_ACCOUNT_DATA["credit_card"]["invoice"]:
            USER_ACCOUNT_DATA["balance"] -= USER_ACCOUNT_DATA["credit_card"]["invoice"]
            USER_ACCOUNT_DATA["credit_card"]["invoice"] = 0
            
            update_account_balance(user_uid , USER_ACCOUNT_DATA["balance"])
            update_credit_invoice(user_uid , USER_ACCOUNT_DATA["credit_card"]["invoice"])
            
            return "Successfully paid invoice"
        
        else:
            return "Insufficient funds!"
            
    except Exception as error:
        return f"An error occurred! {error}"
    
def pay_credit_invoice_with_savings_account(user_uid: str , card_password: str) -> str:
    try:
        USER_ACCOUNT_DATA = get_account_by_uid(user_uid)
        
        if USER_ACCOUNT_DATA is None:
            raise ValueError(f"Error: account with uid {user_uid} not found")
        
        if not pbkdf2_sha256.verify(card_password , USER_ACCOUNT_DATA["card_password_hash"]):
            return "Incorrect card password!"
        
        if USER_ACCOUNT_DATA["savings"] >= USER_ACCOUNT_DATA["credit_card"]["invoice"]:
            USER_ACCOUNT_DATA["savings"] -= USER_ACCOUNT_DATA["credit_card"]["invoice"]
            USER_ACCOUNT_DATA["credit_card"]["invoice"] = 0
            
            update_account_savings(user_uid , USER_ACCOUNT_DATA["savings"])
            update_credit_invoice(user_uid , USER_ACCOUNT_DATA["credit_card"]["invoice"])
            
            return "Successfully paid invoice"
        
        else:
            return "Insufficient funds!"
            
    except Exception as error:
        return f"An error occurred! {error}"
    
def get_statement(uid: str):
    account_data = get_account_by_uid(uid)
    if account_data is None:
        raise ValueError(f"Error: account with uid {uid} not found")
    
    # Check if the "statement" object exists and create it if it does not exist
    if "statement" not in account_data:
        account_data["statement"] = []
    
    return account_data["statement"]
