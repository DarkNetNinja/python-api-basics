"""
Part 3: Dynamic Queries with User Input
=======================================
Difficulty: Intermediate

Learn:
- Using input() to make dynamic API requests
- Building URLs with f-strings
- Query parameters in URLs
"""

import requests


def get_user_info():
    """Fetch user info based on user input."""
    print("=== User Information Lookup ===\n")

    user_id = input("Enter user ID (1-10): ")

    
    if  user_id.isdigit():
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\n--- User #{user_id} Info ---")
            print(f"Name: {data['name']}")
            print(f"Email: {data['email']}")
            print(f"Phone: {data['phone']}")
            print(f"Website: {data['website']}")
        else:
            print(f"\nUser with ID {user_id} not found!")
    else:
        print("userid should be a number")


def search_posts():
    """Search posts by user ID."""
    print("\n=== Post Search ===\n")

    user_id = input("Enter user ID to see their posts (1-10): ")

    # Using query parameters
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": user_id}

    response = requests.get(url, params=params)
    posts = response.json()

    if posts:
        print(f"\n--- Posts by User #{user_id} ---")
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post['title']}")
    else:
        print("No posts found for this user.")


def get_crypto_price():
    """Fetch cryptocurrency price based on user input."""
    print("\n=== Cryptocurrency Price Checker ===\n")

    print("Available coins: btc-bitcoin, eth-ethereum, doge-dogecoin")
    coin_id = input("Enter coin ID (e.g., btc-bitcoin): ").lower().strip()

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price_usd = data['quotes']['USD']['price']
        change_24h = data['quotes']['USD']['percent_change_24h']

        print(f"\n--- {data['name']} ({data['symbol']}) ---")
        print(f"Price: ${price_usd:,.2f}")
        print(f"24h Change: {change_24h:+.2f}%")
    else:
        print(f"\nCoin '{coin_id}' not found!")
        print("Try: btc-bitcoin, eth-ethereum, doge-dogecoin")

def weather_info():
    city = input("Enter city name: ")

    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {"name":city,"count":1}
    geo_response = requests.get(geo_url,params=geo_params)
    geo_data = geo_response.json()
    if not geo_data.get('results'):
        print(f"Error {city} not found")

    geo_data = geo_response.json()
    location = geo_data['results'][0]
    lat = location['latitude']
    long = location['longitude']
    
    print(f"found: {location['name']} lat:{lat} long{long}")


    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude":lat,
              "longitude":long,
              "current_weather":"true"}
    response = requests.get(url,params = params)
    data = response.json()
    
    print(f"Temperature : {data['current_weather']['temperature']}")

def todos_info():
    status = (input("enter status: "))
    if status not in ["true","false"]:
        print("Invalid input")

    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"completed":status}
    
    response = requests.get(url,params = params)
    if response.status_code == 200:
        data = response.json()
        count = len(data)
        print(count)
        print(f"Found {count} todos where completed status = {status}")
        
        if status == "true":
            icon = "✅"
        else:
            icon = "❌"

         

        for i,data in enumerate(data[:5],1):
            print(f"{i}.{icon} {data['title']}")

    remaining = count - 5
    if remaining > 0:
         print(f".... and {remaining} more.")
                
        
    
    
    
    


def main():
    """Main menu for the program."""
    print("=" * 40)
    print("  Dynamic API Query Demo")
    print("=" * 40)

    while True:
        print("\nChoose an option:")
        print("1. Look up user info")
        print("2. Search posts by user")
        print("3. Check crypto price")
        print("4. weather condition")
        print("5. todos_info")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ")

        if choice == "1":
            get_user_info()
        elif choice == "2":
            search_posts()
        elif choice == "3":
            get_crypto_price()
        elif choice == "4":
            weather_info()
        elif choice == "5":
            todos_info()
        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# --- EXERCISES ---
#
# Exercise 1: Add a function to fetch weather for a city
#             Use Open-Meteo API (no key required):
#             https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true
#             Challenge: Let user input city name (you'll need to find lat/long)
#
# Exercise 2: Add a function to search todos by completion status
#             URL: https://jsonplaceholder.typicode.com/todos
#             Params: completed=true or completed=false
#
# Exercise 3: Add input validation (check if user_id is a number)
