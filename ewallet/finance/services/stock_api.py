import requests

API_KEY = "KP5HP5ANEKBE72QE"  # Remplace par ta clé API
#API_KEY = "1X5QGTSJ8FZORWN4"  # Remplace par ta clé API
#API_KEY = "XPB81I0K815170J2"  # Remplace par ta clé API
#API_KEY = "FUU41PKIXK75ZXJ2"
API_URL = "https://www.alphavantage.co/query"

def get_stock_price_old(symbol):
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY
    }
    print("get_stock_price")
    print("symbol")
    print(symbol)
    response = requests.get(API_URL, params=params)
    data = response.json()
    
    print("data")
    print(data)
    
    try:
        return float(data["Global Quote"]["05. price"])  # Prix actuel
    except KeyError:
        return None  # En cas d'erreur




import requests

API_KEY = "P5PuKDmXNiltclmPsSTnrph3X8anpjNv"
API_URL = "https://financialmodelingprep.com/api/v3/quote"

def get_stock_price(symbol):
    params = {
        "apikey": API_KEY
    }
    url = f"{API_URL}/{symbol}"
    response = requests.get(url, params=params)
    data = response.json()
    
    print("data")
    print(data)
    
    try:
        return float(data[0]["price"])  # Prix actuel
    except (KeyError, IndexError):
        return None  # En cas d'erreur