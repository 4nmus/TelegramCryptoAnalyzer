import requests
import time


def get_bitcoin_price() -> float:
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    data = response.json()
    return float(data["price"])

def calculate_percentage_change(old_price, new_price) -> float:
    change = ((new_price - old_price) / old_price) * 100
    return change

def track_bitcoin_price_with_alert():
    print("Start..")

    old_price = get_bitcoin_price()
    print(f"Initial Bitcoin price: ${old_price:.2f}")

    while True:
        time.sleep(3)

        new_price = get_bitcoin_price()
        print(f"New Bitcoin price: ${new_price:.2f}")

        price_change = calculate_percentage_change(old_price, new_price)
        print(f"Bitcoin price changed by: {price_change:.2f}%")

        if abs(price_change) >= 3:
            if price_change > 0:
                print(f"Alert: Bitcoin price increased by more than 3%!")
            else:
                print(f"Alert: Bitcoin price decreased by more than 3%!")
            old_price = new_price



if __name__ == "__main__":
    track_bitcoin_price_with_alert()
