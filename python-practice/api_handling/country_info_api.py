import requests

country = input("Enter Country Name: ")

url = f"https://restcountries.com/v3.1/name/{country}"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    if isinstance(data, list):
        print("Country:", data[0]["name"]["common"])
        print("Capital:", data[0]["capital"][0])
        print("Population:", data[0]["population"])
    else:
        print("Unexpected API Response")
        print(data)

else:
    print("Country Not Found")