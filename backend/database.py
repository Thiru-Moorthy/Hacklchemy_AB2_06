import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["darkweb"]
collection = db["threat_data"]

# Ensure collection exists
if "threat_data" not in db.list_collection_names():
    db.create_collection("threat_data")
