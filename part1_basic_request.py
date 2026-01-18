"""
Part 1: Basic GET Request
=========================
Difficulty: Beginner

Learn: How to make a simple GET request and view the response.

We'll use JSONPlaceholder - a free fake API for testing.
"""

import requests

# Step 1: Define the API URL
url = "https://jsonplaceholder.typicode.com/posts/5"

# Step 2: Make a GET request
response = requests.get(url)
print(type(response))
print(response)

# Step 3: Print the response
print("=== Basic API Request ===\n")
print(f"URL: {url}")
print(f"Status Code: {response.status_code}")
print(f"\nResponse Data:")
print(response.json())


url = "https://api.coinpaprika.com/v1/coins/btc-bitcoin"
response1 = requests.get(url)
print(type(response1))
print(response1)

print(response1.json())

url = "https://api.open-meteo.com/v1/forecast"

params = {"latitude":28.61,
          "longitude":77.23,
          "current_weather":"true"}

headers = {"Accept": "application/json"}

response = requests.get(url,params=params,headers=headers)

print(response.status_code)
print(response.json())
print("Current temp:",response.json()['current_weather']['temperature'])

url = "https://jsonplaceholder.typicode.com/users"

response4 = requests.get(url)
print(len(response4.json()))

url = "https://jsonplaceholder.typicode.com/posts/999"

response5 = requests.get(url)
print(response5.json())

# for user in response4:
#     print(user[0]['name'])



# --- EXERCISES ---
# Try these on your own:
#
# Exercise 1: Change the URL to fetch post number 5
#             Hint: Change /posts/1 to /posts/5
#
# Exercise 2: Fetch a list of all users
#             URL: https://jsonplaceholder.typicode.com/users
#
# Exercise 3: What happens if you fetch a post that doesn't exist?
#             Try: https://jsonplaceholder.typicode.com/posts/999
 #            Ans: It has shown an empty dictionary {}
