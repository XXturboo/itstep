import requests

# response = requests.get("https://api.monobank.ua/bank/currency")
# data = response.json()
#
# usdSell = data[0]["rateSell"]
#
# sun = int(input("Input sun of the UAH you have: "))
#
# print("You have: $", round((sun / usdSell), 4))

def clean_and_convert(price):
    return float(price.replace(',', '').replace('$', ''))

prices = []

response = requests.get("https://coinmarketcap.com/")
data = response.text
parse_data = data.split("<span>")
for item in parse_data:
    if item.startswith("$"):
        for price in item.split("</span>"):
            if price.startswith("$") and price[1].isdigit():
                prices.append(price)
                break


# bit_coin = prices[0].replace(',','').replace('$','')
# print("Bitcoin price: ", bit_coin)

bitcoin_amount = float(input("Enter the amount of your bitcoins: "))

total_value = clean_and_convert(prices[0]) * bitcoin_amount

print(f"Price {bitcoin_amount} bitcoin makes up: ${total_value:.2f}")
