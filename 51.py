exchange_rates = {
    "USD": 1.0,
    "EUR": 0.861775,
    "GBP": 0.726763,
    "INR": 75.054725,
    "AUD": 1.333679,
    "CAD": 1.237816,
    "SGD": 1.346851,
}

def convert(x,y,n):
    a=exchange_rates[y]/exchange_rates[x]*n
    return round(a,2)


currency = convert("EUR", "USD", 100)
print(currency)