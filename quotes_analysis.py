import statistics

from pymongo import MongoClient

# Create a MongoDB Connection
client = MongoClient('mongodb://localhost:27017/')

# Connect to the Database and it's collection
db = client.project.Google

results = db.find()

for record in results:
    data = record['query']['results']['row']

total = []
for i in data:
    total.append(float(i['col6']))

print('Mean Price for Google Stock: ',statistics.mean(total))

#print('Median Price for Google Stock: ',statistics.median(total))

#print('Standard Deviation Price for Google Stock: ',statistics.stdev(total))
