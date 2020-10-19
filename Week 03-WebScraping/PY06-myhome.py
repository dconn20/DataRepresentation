# read data from website

import requests
import csv
from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale")

soup = BeautifulSoup(page.content, 'html.parser')

home_file = open('MyHome.csv', mode = 'w')
home_writer = csv.writer(home_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


listings = soup.find("div", class_="PropertyListingCard" )

for listing in listings:
    entryList = []

    price = listings.find(class_="PropertyListingCard_Price")
    entryList.append(price)
    address = listings.find(class_="PropertyListingCard_Address")
    entryList.append(address)

    home_writer.writerow(entryList)
home_file.close()