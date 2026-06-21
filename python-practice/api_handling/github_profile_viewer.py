import requests

username = input("Enter GitHub Username: ")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    print("\nGitHub Profile")
    print("-------------------")
    print("Name:", data["name"])
    print("Username:", data["login"])
    print("Followers:", data["followers"])
    print("Following:", data["following"])
    print("Public Repositories:", data["public_repos"])

else:
    print("User Not Found")