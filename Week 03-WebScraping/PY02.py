# Test BeautifulSoup

import requests
from bs4 import BeautifulSoup
page = requests.get("https://github.com/dconn20/DataRepresentation")
print(page)
print("-----------------")
print(page.content)
soup1 = BeautifulSoup(page.content, 'html.parser')
print("-----------------")
print(soup1.prettify())