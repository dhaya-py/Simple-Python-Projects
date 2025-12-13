from currency_converter import CurrencyConverter

c = CurrencyConverter()

amount = input("Enter the amount :")
from_currency = input("From currency :").upper()
to_currency = input("To currency :").upper()

result = c.convert(amount, from_currency, to_currency)

print(result)

