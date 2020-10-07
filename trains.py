# Damien Connolly
# Write a program that stores the data for all 
# trains in Ireland in a csv file.

import requests
import csv
from bs4 import BeautifulSoup

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'xml')
#print (soup.prettify())

retrievetags=['TrainStatus', 
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction']



with open('week03_south.csv', mode = 'w') as south_file:
    south_writer = csv.writer(south_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    listings = soup.findAll("objTrainPositions")
    for listing in listings:
        lat = float(listing.TrainLatitude.string)
        if (lat < 53.4):
        #print(listing.TrainLatitude.string) 


            entryList = []
            for retrievetag in retrievetags:
            #print (listing.find(retrievetag).string) 
                entryList.append(listing.find(retrievetag).string)
        south_writer.writerow(entryList)
