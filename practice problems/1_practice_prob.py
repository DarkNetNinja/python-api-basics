import requests

# user_input = input("Enter the useid(1-200)")

# url = f"https://jsonplaceholder.typicode.com/todos/{user_input}"
# response = requests.get(url)
# print(response.json())
# if response.status_code == 200:
#     data = response.json()
#     print(f"{data['title']}")
# else:
#     print(f"{user_input} not found")

def find_info():
    id = input("Enter userid: ")
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(url)


    if response.status_code == 200:

        data = response.json()
        print(f"{data['address']['street']}")
    elif response.status_code == 404:
        print(f"{id} not available")

find_info()
