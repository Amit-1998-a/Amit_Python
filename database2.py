# importing Mongoclient from pymongo
from pymongo import MongoClient



myclient = MongoClient("mongodb://localhost:27017/")

# database
db = myclient["Amit"]


collection = db["Student"]


records = {
	"record1": { "_id": 6,
	"name": "Karan",
	"Roll No": "5",
	"Branch": "entc"},

	"record2": { "_id": 7,
	"name": "aditya",
	"Roll No": "6",
	"Branch": "entc"}
}

app=collection.find().sort("name")

for x in app:
	print(x)


print("all inserted")