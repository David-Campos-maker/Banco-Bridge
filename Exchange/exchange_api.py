import json
import os

RATES_DATA_PATH = os.path.join(os.path.dirname(__file__) , 'rates.json')

def get_currency_rate_by_code(currency_code: str): 
    with open(RATES_DATA_PATH , "r") as rates_data_file:
        rates_data = json.load(rates_data_file)
        
    try:
        return rates_data['exchange'][currency_code]['rates']
    
    except KeyError:
        print(f"Currency code not found! {currency_code}")
        return None