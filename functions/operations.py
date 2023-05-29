import sys
sys.path.insert(1 , '../functions/utils')
sys.path.insert(2 , "../Exchange")
from account_helpers import get_account_by_uid
from exchange_api import get_currency_rate_by_code

# account_data = get_account_by_uid(1234)

# currency_code: str = "cny"

# print(get_currency_rate_by_code(currency_code.upper()))
    
# print(account_data)

def transfer(debtors_uid: int , creditors_uid: int , transfer_amount: float):
    debtors_account_data = get_account_by_uid(debtors_uid)
    creditors_account_data = get_account_by_uid(creditors_uid)
    
    print(debtors_account_data)
    print(creditors_account_data)
    
    
creditors_account = int(input('creditor`s account uid: '))
debtors_account = int(input('debtor`s account uid: '))

transfer(debtors_account , creditors_account , 20.00)
    
    
# debtors_account_uid = 1234
# debtors_account_balance = 100.00
# debtors_account_currency = 'BRL'

# creditor_account_uid = 1
# creditor_account_balance = 300.00
# creditor_account_currency = 'USD'

# value_to_be_exchanged = 10.00

# debtors_account_balance = debtors_account_balance - (value_to_be_exchanged * exchanges_data[creditor_account_currency]['rates'][debtors_account_currency])
# creditor_account_balance = creditor_account_balance + (value_to_be_exchanged * exchanges_data[debtors_account_currency]['rates'][creditor_account_currency])

# print('debtor`s balance -> ' + str(debtors_account_balance))
# print('credtor`s balance -> ' + str(creditor_account_balance))