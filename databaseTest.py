import pandas as pd

data = pd.read_json("database.json")
print(data)

for account in data.accounts:
    print(account["name"])
