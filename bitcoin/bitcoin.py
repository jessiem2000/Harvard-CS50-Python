import requests
import sys
import json
global amount, cost

def main():
    try:
        digit = sys.argv[1]
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")

        elif float_check(digit) == True:
            amount = float(digit)
            cost = bitcoin_price(amount)
            print(f"${cost:,.4f}")
    except requests.RequestException:
        pass


def float_check(digit):
    try:
        float(digit)
        return True
    except ValueError:
        sys.exit("Command-line argument is not a number")


def bitcoin_price(amount):
        url = "https://rest.coincap.io/v3/assets/bitcoin?&apiKey=f21d2d58b71b63028ecf3cf1f97fd3b0df07af117711b38b6a26d9939ae90da7"
        r = requests.get(url)
        b = r.json()
        btc = float(b['data']['priceUsd'])
        btc = round(btc, 4)
        cost = eval(f"{btc}*{amount}")
        return cost

main()


