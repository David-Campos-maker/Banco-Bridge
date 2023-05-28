import sys
sys.path.insert(1 , "./functions/utils")
from database_helpers import get_accounts_data
from account_helpers import get_account_by_uid

get_accounts_data()
print(get_account_by_uid(1234))