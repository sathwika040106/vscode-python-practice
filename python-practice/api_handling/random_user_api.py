import requests

url = "https://randomuser.me/api/"

response = requests.get(url)

data = response.json()

user = data["results"][0]

print("Name:", user["name"]["first"])
print("Email:", user["email"])
print("Country:", user["location"]["country"])