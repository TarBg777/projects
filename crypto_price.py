import requests

def get_crypto_price(crypto="bitcoin", currency="usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"
    response = requests.get(url)
    if response.status_code == 200:
        price = response.json()[crypto][currency]
        print(f"{crypto.capitalize()} price: {price} {currency.upper()}")
    else:
        print("Error fetching data")

if __name__ == "__main__":
    get_crypto_price("ethereum", "usd")
