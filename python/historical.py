import requests

def get_coin_history(coin_id, days=30):

    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"

    params = {
        "vs_currency" : "usd",
        "days" : days,
        "interval" : "daily" 
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.RequestException:
        return None