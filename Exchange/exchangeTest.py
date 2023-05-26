import json

with open("../database.json" , "r") as data_base_file:
    data_base = json.load(data_base_file)
    exchanges_data = data_base['exchanges']
    
debtors_account_uid = 1234
debtors_account_balance = 100.00
debtors_account_currency = 'BRL'

creditor_account_uid = 1
creditor_account_balance = 300.00
creditor_account_currency = 'USD'

value_to_be_exchanged = 10.00

debtors_account_balance = debtors_account_balance - (value_to_be_exchanged * exchanges_data[creditor_account_currency]['rates'][debtors_account_currency])
creditor_account_balance = creditor_account_balance + (value_to_be_exchanged * exchanges_data[debtors_account_currency]['rates'][creditor_account_currency])

print('debtor`s balance -> ' + str(debtors_account_balance))
print('credtor`s balance -> ' + str(creditor_account_balance))
