from functions.utils.account_helpers import get_account_by_uid
from functions.utils.database_helpers import update_account_balance , update_account_savings
from Exchange.exchange_api import get_currency_rate_by_code

def transfer(debtors_uid: str , creditors_uid: str , transfer_amount: float) -> str:
    try:
        DEBTORS_ACCOUNT_DATA = get_account_by_uid(debtors_uid)
        if DEBTORS_ACCOUNT_DATA is None:
            raise ValueError(f"Error: account with uid {debtors_uid} not found")
        
        CREDITORS_ACCOUNT_DATA = get_account_by_uid(creditors_uid)
        if CREDITORS_ACCOUNT_DATA is None:
            raise ValueError(f"Error: account with uid {creditors_uid} not found")
        
        DEBTORS_CURRENCY_RATES = get_currency_rate_by_code(DEBTORS_ACCOUNT_DATA["currency"])
        if DEBTORS_CURRENCY_RATES is None:
            raise ValueError(f"Error: currency rate for {DEBTORS_ACCOUNT_DATA['currency']} not found")
        
        amount_to_be_debited = transfer_amount * DEBTORS_CURRENCY_RATES[CREDITORS_ACCOUNT_DATA["currency"]] * 0.0425
        
        if DEBTORS_ACCOUNT_DATA["balance"] >= amount_to_be_debited:
            CREDITORS_ACCOUNT_DATA["balance"] += transfer_amount
            DEBTORS_ACCOUNT_DATA["balance"] -= amount_to_be_debited
            
            update_account_balance(creditors_uid , CREDITORS_ACCOUNT_DATA["balance"])
            update_account_balance(debtors_uid , DEBTORS_ACCOUNT_DATA["balance"])
            
            return "Transaction successful!"
        
        else:
            CREDITORS_ACCOUNT_DATA["balance"] += transfer_amount
            DEBTORS_ACCOUNT_DATA["balance"] -= amount_to_be_debited * 0.1
            
            update_account_balance(creditors_uid , CREDITORS_ACCOUNT_DATA["balance"])
            update_account_balance(debtors_uid , DEBTORS_ACCOUNT_DATA["balance"])
            
            return "Insufficient funds! The transfer was completed generating a debt of 10%" 
        
    except Exception as error:
        return f"An error occurred! {error}"

def transfer_with_savings_account(debtors_uid: str , creditors_uid: str , transfer_amount: float) -> str:
    try:
        DEBTORS_ACCOUNT_DATA = get_account_by_uid(debtors_uid)
        if DEBTORS_ACCOUNT_DATA is None:
            raise ValueError(f"Error: account with uid {debtors_uid} not found")
        
        CREDITORS_ACCOUNT_DATA = get_account_by_uid(creditors_uid)
        if CREDITORS_ACCOUNT_DATA is None:
            raise ValueError(f"Error: account with uid {creditors_uid} not found")
        
        DEBTORS_CURRENCY_RATES = get_currency_rate_by_code(DEBTORS_ACCOUNT_DATA["currency"])
        if DEBTORS_CURRENCY_RATES is None:
            raise ValueError(f"Error: currency rate for {DEBTORS_ACCOUNT_DATA['currency']} not found")
        
        amount_to_be_debited = transfer_amount * DEBTORS_CURRENCY_RATES[CREDITORS_ACCOUNT_DATA["currency"]] * 0.0425
        
        if DEBTORS_ACCOUNT_DATA["savings"] >= amount_to_be_debited:
            CREDITORS_ACCOUNT_DATA["balance"] += transfer_amount
            DEBTORS_ACCOUNT_DATA["savings"] -= amount_to_be_debited
            
            update_account_balance(creditors_uid , CREDITORS_ACCOUNT_DATA["balance"])
            update_account_savings(debtors_uid , DEBTORS_ACCOUNT_DATA["savings"])
            
            return "Transaction successful!"
        
        else:
            CREDITORS_ACCOUNT_DATA["balance"] += transfer_amount
            DEBTORS_ACCOUNT_DATA["savings"] -= amount_to_be_debited * 0.1
            
            update_account_balance(creditors_uid , CREDITORS_ACCOUNT_DATA["balance"])
            update_account_savings(debtors_uid , DEBTORS_ACCOUNT_DATA["savings"])
            
            return "Insufficient funds! The transfer was completed generating a debt of 10%" 
        
    except Exception as error:
        return f"An error occurred! {error}"
    
def deposit_into_savings_account(user_uid: str , deposit_amount: float) -> str:
    try:
        USER_ACCOUNT_DATA = get_account_by_uid(user_uid)
        
        if USER_ACCOUNT_DATA is None:
            raise ValueError(f"Error: account with uid {user_uid} not found")
        
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