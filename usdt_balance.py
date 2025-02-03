from web3 import Web3

INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
USDT_CONTRACT = "0xdAC17F958D2ee523a2206206994597C13D831ec7"

web3 = Web3(Web3.HTTPProvider(INFURA_URL))

usdt_abi = '[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}]'

contract = web3.eth.contract(address=USDT_CONTRACT, abi=usdt_abi)

def get_usdt_balance(wallet_address):
    balance = contract.functions.balanceOf(wallet_address).call()
    return balance / 10**6  # USDT має 6 десяткових знаків

if __name__ == "__main__":
    wallet = input("Enter Ethereum wallet address: ")
    print(f"USDT Balance: {get_usdt_balance(wallet)} USDT")
