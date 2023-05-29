from functions.utils.account_helpers import get_account_by_uid
from functions.utils.database_helpers import update_account_balance
from Exchange.exchange_api import get_currency_rate_by_code

def transfer(debtors_uid: int , creditors_uid: int , transfer_amount: float):
    DEBTORS_ACCOUNT_DATA = get_account_by_uid(debtors_uid)
    CREDITORS_ACCOUNT_DATA = get_account_by_uid(creditors_uid)
    
    DEBTORS_CURRENCY_RATES = get_currency_rate_by_code(DEBTORS_ACCOUNT_DATA['currency'])
    CREDITORS_CURRENCY_RATES = get_currency_rate_by_code(CREDITORS_ACCOUNT_DATA['currency'])
    
    debtors_balance = DEBTORS_ACCOUNT_DATA['balance']
    creditors_balance = CREDITORS_ACCOUNT_DATA["balance"]
    
    if debtors_balance >= (transfer_amount * DEBTORS_CURRENCY_RATES[CREDITORS_ACCOUNT_DATA['currency']]):
        creditors_balance = creditors_balance + (transfer_amount * CREDITORS_CURRENCY_RATES[DEBTORS_ACCOUNT_DATA['currency']])
        debtors_balance = debtors_balance - (transfer_amount * DEBTORS_CURRENCY_RATES[CREDITORS_ACCOUNT_DATA['currency']])
        
        update_account_balance(creditors_uid , creditors_balance)
        update_account_balance(debtors_uid , debtors_balance)
    
    else:
        print("Insufficient funds!")

    
creditors_account = int(input('creditor`s account uid: '))
debtors_account = int(input('debtor`s account uid: '))
tranfer_amount = float(input('Tranfer amount: '))


transfer(debtors_account , creditors_account , tranfer_amount)

print(get_account_by_uid(creditors_account))
print(get_account_by_uid(debtors_account))
    