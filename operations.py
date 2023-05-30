from functions.transactions import transfer
from functions.utils.account_helpers import get_account_by_uid   
    
creditors_account = str(input('creditor`s account uid: '))
debtors_account = str(input('debtor`s account uid: '))
tranfer_amount = float(input('Tranfer amount: '))

transfer(debtors_account , creditors_account , tranfer_amount)

print(get_account_by_uid(creditors_account))
print(get_account_by_uid(debtors_account))
    