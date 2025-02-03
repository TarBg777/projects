import requests
import matplotlib.pyplot as plt

def get_price_history(crypto="bitcoin", currency="usd", days=7):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto}/market_chart?vs_currency={currency}&days={days}"
    response = requests.get(url)
    if response.status_code == 200:
        prices = response.json()['prices']
        return [price[1] for price in prices]
    return []

def plot_price_chart(prices, crypto="Bitcoin"):
    plt.plot(prices, label=f"{crypto} Price")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.title(f"{crypto} Price Chart")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    data = get_price_history()
    if data:
        plot_price_chart(data)
    else:
        print("Error fetching data")
