import urllib2
import json
import csv

from pymongo import MongoClient

# Create a MongoDB Connection
client = MongoClient('mongodb://localhost:27017/')

# Connect to the Database and it's collection
db = client.project.quotes

# Create the TSV file


results = db.find()

# For Closing Price
for record in results:
    data = record['query']['results']['row']
    fileName = record['query']['symbol']
    with open(fileName+'.csv', 'wb') as csvfile:
        fieldnames = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for i in data:
            writer.writerow({'Date': str(i['col0']), 'Open': str(i['col1']), 'High': str(i['col2']), 'Low': str(i['col3']), 'Close': str(i['col4']), 'Volume': str(i['col5'])})
