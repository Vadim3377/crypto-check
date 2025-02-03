import requests

import datetime
from web3 import Web3

def get_price_data():

    url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart"

    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=360)

    params = {
        'vs_currency': 'usd',
        'days': (end_date - start_date).days
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Extracting price data
    prices = data.get('prices', [])
    return prices

prices = get_price_data()
def Search(timestamp,amount):
    #print(prices)
    for i in range(len(prices)):
        if prices[i][0] // 100000000 == timestamp:
            return prices[i][1]*amount
    return 0

def get_transactions(api_key, wallet_address):

    url = f"https://api.etherscan.io/api"
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=360)

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

    # Request transaction data
    response = requests.get(url, params=params)
    transactions = response.json()['result']

    recent_transactions = [
        tx for tx in transactions
        if datetime.datetime.fromtimestamp(int(tx['timeStamp'])) >= start_date
    ]
    purchases = []
    sales = []
    # Display transactions
    for tx in recent_transactions:
        res = Web3.from_wei(int(tx['value']),'ether')
        if res<100 and res > 0.0000001:
            #print(int(tx['timeStamp'])//100000)
            usd = Search(int(tx['timeStamp'])//100000,float(res))
            if tx['from'].lower() == wallet_address.lower():
                sales.append(usd)
            if tx['to'].lower() == wallet_address.lower():
                purchases.append(usd)
    return purchases, sales
def getROI(WALLET_ADDRESS):
    API_KEY = '4INST6C9GE4BP9DYMAKCVRXF8UK1TY9FD5'
    purchases, sales = get_transactions(API_KEY,WALLET_ADDRESS)
    #print(purchases)

    total_buys = sum(purchases)
    total_sales = sum(sales)

    #print(total_buys)
    #print(total_sales)
    if total_buys > 0:
        roi = (total_sales / total_buys)
    else:
        roi = 0
    return (roi)

