import requests

username = input("Enter GitHub Username: ")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    print("Name:", data.get("name"))
    print("Followers:", data.get("followers"))
    print("Public Repos:", data.get("public_repos"))

else:
    print("User Not Found")