# importing Mongoclient from pymongo
from pymongo import MongoClient

# Making Connection
myclient = MongoClient("mongodb://localhost:27017/")

# database
db = myclient["Amit"]


collection = db["Student"]

# Creating Dictionary of records to be
# inserted
record = { "_id": 5,
		"name": "Raju",
		"Roll No": "1005",
		"Branch": "CSE"}



# record1 in the collection
#  collection.insert_one()
rec_id1 = collection.insert_one(record)



