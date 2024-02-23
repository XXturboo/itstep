import requests

response = requests.get("https://api.monobank.ua/bank/currency")
data = response.json()
usdSell = data[0]["rateSell"]
eurSell = data[1]["rateSell"]
gbpSell = data[2]["rateSell"]


sun = int(input("Input sun of the UAH you have: "))

print("You have: $", round((sun / usdSell), 4))
print("You have: €", round((sun / eurSell), 4))
print("You have: £", round((sun / gbpSell), 4))