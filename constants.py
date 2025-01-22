from web3 import Web3

def amount(tx_hash):
  infura_url = 'https://mainnet.infura.io/v3/4888777348134db7a3307956f68cd8c0'
  web3 = Web3(Web3.HTTPProvider(infura_url))


  receipt = web3.eth.get_transaction_receipt(tx_hash)
  erc20_abi = '''
  [
    {"anonymous": false,"inputs": 
        [
            {"indexed": true, "name": "from", "type": "address"},
            {"indexed": true, "name": "to", "type": "address"},
            {"indexed": false, "name": "value", "type": "uint256"}
        ],
    "name": "Transfer","type": "event"}
  ]
  '''


  contract = web3.eth.contract(abi=erc20_abi)

# Decode all Transfer events from logs
  transfers = []
  for log in receipt.logs:
    try:
        decoded_log = contract.events.Transfer().processReceipt({'logs': [log]})
        if decoded_log:
            transfers.append(decoded_log[0]['args'])
    except Exception as e:
        print("No Transfer event found in this log:", e)
