from transformers import pipeline
import pymongo

# Load MongoDB Data
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["darkweb"]
collection = db["threat_data"]

# Load NER Model
ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

# Extract Sensitive Data
for doc in collection.find():
    text = doc["data"]
    entities = ner(text)
    collection.update_one({"_id": doc["_id"]}, {"$set": {"entities": entities}})
    print(f"🔎 {doc['url']} → {entities}")
