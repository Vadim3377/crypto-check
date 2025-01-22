from web3 import Web3
import requests
from datetime import datetime


def get_token_price_at_transaction(token_id, transaction_hash):
    provider = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/4888777348134db7a3307956f68cd8c0'))
    transaction = provider.eth.get_transaction(transaction_hash)
    block = provider.eth.get_block(transaction["blockNumber"])

    date = format_timestamp(block.timestamp)
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/{token_id}/history?date={date}")
    data = response.json()

    return data['market_data']['current_price']['usd']


def format_timestamp(timestamp):
    date = datetime.utcfromtimestamp(timestamp)
    return date.strftime('%d-%m-%Y')  # Format date as DD-MM-YYYY


def run(transaction_hash):
    token_id = 'ethereum'
    price = 0
    try:
        price = get_token_price_at_transaction(token_id, transaction_hash)
        return price
    except Exception as e:
        #print("Not Found")
        return 0
