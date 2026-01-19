import requests

def get_crypto_price():
    coin_id = input("Enter coin id: ").lower().strip()
    
    url =  f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
    response = requests.get()
    

    if response.status_code == 200:
        
        data = response.json()
        price_usd = data['quotes']['USD']['price']
        change_24h = data['quotes']['USD']['percent_change_24h']

        print(f"  {data['name']} {data['symbol']}")
        print(f"price {price_usd:,.2f}")
        print(f"24h change {change_24h:+.2f}")
    else:
        print(f"{coin_id} not found")


url = "https://api.open-meteo.com/v1/forecast"

params = {"latitude":28.61,"longitude":77.63,"current_weather":"true"}

response = requests.get(url,params=params)

data = response.json()
print(f"{data['current_weather']}")