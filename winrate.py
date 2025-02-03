import requests
from datetime import datetime, timedelta

# API Key from Etherscan or another blockchain service provider

def fetch_transactions(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['result']
    else:
        raise Exception("Failed to fetch transactions")


def compute_win_rate(wallet_address, transactions):

    profit_making = 0
    total = 0
    purchase_price = {}
    for tx in transactions:
        value = tx['value']
        token = tx['tokenSymbol']
        if tx['to'].lower() == wallet_address.lower():
            purchase_price[token] = value
        elif tx['from'].lower() == wallet_address.lower():
            if token in purchase_price and (int(value) - int(purchase_price[token]) > 0):
                profit_making += 1
            total += 1

    return (profit_making / total) if total > 0 else 0

def main(wallet_adress):
    api_key = '4INST6C9GE4BP9DYMAKCVRXF8UK1TY9FD5'

    # Ethereum wallet address

    # Define the endpoint URL
    url = f"https://api.etherscan.io/api?module=account&action=tokentx&address={wallet_adress}&startblock=0&endblock=999999999&sort=asc&apikey={api_key}"
    transactions = fetch_transactions(url)
    return (compute_win_rate(wallet_adress,transactions))*100

