import requests
from decouple import config

#API_KEY = "P5PuKDmXNiltclmPsSTnrph3X8anpjNv"
API_KEY = config('API_KEY')
API_URL = "https://financialmodelingprep.com/api/v3/quote"

def get_stock_price(symbol):
    params = {
        "apikey": API_KEY
    }
    url = f"{API_URL}/{symbol}"
    response = requests.get(url, params=params)
    data = response.json()
    
    try:
        return float(data[0]["price"])  # Prix actuel
    except (KeyError, IndexError):
        return None  # En cas d'erreur