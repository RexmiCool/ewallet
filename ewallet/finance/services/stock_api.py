import requests

API_KEY = "1X5QGTSJ8FZORWN4"  # Remplace par ta clé API
API_URL = "https://www.alphavantage.co/query"

def get_stock_price(symbol):
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    
    try:
        return float(data["Global Quote"]["05. price"])  # Prix actuel
    except KeyError:
        return None  # En cas d'erreur
