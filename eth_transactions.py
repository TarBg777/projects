from web3 import Web3

# Підключення до Ethereum RPC (Infura)
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

def get_latest_transactions():
    latest_block = web3.eth.block_number
    block = web3.eth.get_block(latest_block, full_transactions=True)
    for tx in block.transactions[:5]:  # Виведемо перші 5 транзакцій
        print(f"Tx Hash: {tx.hash.hex()}")
        print(f"From: {tx['from']} -> To: {tx['to']}")
        print(f"Value: {web3.fromWei(tx.value, 'ether')} ETH\n")

if __name__ == "__main__":
    get_latest_transactions()
