import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

headings = soup.find_all("h1")

for heading in headings:
    print(heading.text)