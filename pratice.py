exchange_rate ={

        "INR" : 84.50,
        "EUR" : 0.92,
        "GBP" : 0.78,
        "JPY" : 150.20
        }
def exchange_to_usd(amount, currency):
    try:
        rate = exchange_rate[currency]
        f_RATE = amount/rate
        print(round(f_RATE, 2))
        return(round(f_RATE, 2))
    except TypeError:
     print("enter valid curency in number insitad of text")
exchange_to_usd(500, "INR")