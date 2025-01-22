import requests
import data_classes
import constants
from datetime import datetime, timedelta

def get_transactions(api_key, wallet_address):
    url = f"https://api.etherscan.io/api"
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    # Parameters for the API call
    params = {
        'module': 'account',
        'action': 'tokentx',
        'address': wallet_address,
        'startblock': 0,
        'endblock': 99999999,
        'sort': 'asc',
        'apikey': api_key
    }


    response = requests.get(url, params=params)
    transactions = response.json()['result']
    # print(len(transactions))
    # Filter transactions from the last 7 days
    recent_transactions = [
        tx for tx in transactions
        if datetime.fromtimestamp(int(tx['timeStamp'])) >= start_date
    ]
    #tokenAmounts = constants.CalcAmount(wallet_address)
    #print(tokenAmounts)
    purchases = []
    sales = []
    i = 0
    for tx in recent_transactions:
        #amount = tokenAmounts[i]
        if tx['from'].lower() == wallet_address.lower():
            print(tx['hash'])
            print(constants.amount(tx['hash']))
            priceUSD = data_classes.run(tx['hash'])
            #sales.append((tx['tokenSymbol'], priceUSD*amount))
        if tx['to'].lower() == wallet_address.lower():
            priceUSD = data_classes.run(tx['hash'])
            #purchases.append((tx['tokenSymbol'], priceUSD * amount,tx['timeStamp']))
        i+=1

    print(sales)
    print(purchases)

get_transactions('4INST6C9GE4BP9DYMAKCVRXF8UK1TY9FD5','0x5dc0bd524348096bc7ddc4291eee3750a1a29b7c')