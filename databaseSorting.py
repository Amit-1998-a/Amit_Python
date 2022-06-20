# python code to sort elements
# alphabetically in ascending order

import pymongo

# establishing connection
# to the database
my_client = pymongo.MongoClient('localhost', 27017)

# Name of the database
mydb = my_client["Amit"]

# Name of the collection
mynew = mydb["Student"]


record = { "_id": 5,
		"name": "Raju",
		"Roll No": "1005",
		"Branch": "CSE"}


# sorting function
mydoc = mynew.find().sort("name")

for x in mydoc:
    print(x)