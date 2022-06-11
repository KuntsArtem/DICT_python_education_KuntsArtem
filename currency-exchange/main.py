import json
import requests
user_currency = input("Сhoose which currency you have >")
user_currency_counter = float(input("How many " + str(user_currency) + " you have >?"))
user_check = {}
currency_rates = {}
while user_currency_counter != 0:
    quantity = float(input("How many " + str(user_currency) + " do you want to exchange >"))
    currency_to_buy = input("Which currency do you want to buy? >")
    while quantity > user_currency_counter:
        print("You have only " + str(user_currency_counter) + " " + str(user_currency))
        quantity = float(input("How many " + str(user_currency) + " do you want to exchange >"))
    user_currency_counter = user_currency_counter - quantity
    if currency_to_buy not in currency_rates.keys():
        res = requests.get('http://www.floatrates.com/daily/' + str(user_currency) + '.json')
        data = json.loads(res.text)
        datacurrency = round(data.get(str(currency_to_buy)).get('rate'), 2)
        user_check.update([(currency_to_buy, quantity * datacurrency)])
        currency_rates.update([(currency_to_buy, round(datacurrency, 2))])
        print("You received " + currency_to_buy + " " + str(round(user_check.get(currency_to_buy), 2)))
    else:
        print("It is in cashe!")
        user_check.update([(currency_to_buy, quantity * currency_rates.get(currency_to_buy))])
        print("You received " + currency_to_buy + " " + str(round(user_check.get(currency_to_buy), 2)))
print("You alredy have :")
for key, value in user_check.items():
        print((key, value), "\n")
