import requests
import time
from web3 import Web3


def get_transactions(api_key, address):
    # Current time and time one hour ago in Unix time
    current_time = int(time.time())
    one_hour_ago = current_time - 3600*24*7

    # Setup API request URL
    endpoint = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'tokentx',
        'address': address,
        'startblock': 0,
        'endblock': 99999999,
        'sort': 'asc',
        'apikey': api_key
    }

    response = requests.get(endpoint, params=params)
    transactions = response.json()

    # Filter transactions from the last hour
    recent_transactions = [tx for tx in transactions['result']
                           if int(tx['timeStamp']) >= one_hour_ago]
    mes = ""
    for tx in recent_transactions:
        if tx['to'].lower() == address.lower():
            amount = Web3.from_wei(int(tx['value']), 'ether')
            mes += "Purchased:" + "\n" + tx["tokenSymbol"] + "\n" + "Amount: " + str(amount) + " eth" + "\n"
        elif tx['from'].lower() == address.lower():
            amount = Web3.from_wei(int(tx['value']),'ether')
            mes += "Sold" + " " + tx["tokenSymbol"] + "\n" + "Amount: " + str(amount) + " eth" + "\n"
    return mes

def run(wallet_address):
    # Insert your Etherscan API Key here
    api_key = "4INST6C9GE4BP9DYMAKCVRXF8UK1TY9FD5"

    recent_txs = get_transactions(api_key, wallet_address)

    return recent_txs
