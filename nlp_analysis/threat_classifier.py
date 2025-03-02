from transformers import pipeline
import pymongo

# Load MongoDB Data
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["darkweb"]
collection = db["threat_data"]

# Load NLP Model
classifier = pipeline("text-classification", model="facebook/bart-large-mnli")

# Process Dark Web Data
for doc in collection.find():
    text = doc["data"]
    result = classifier(text, candidate_labels=["hacking", "data breach", "malware", "phishing"])
    collection.update_one({"_id": doc["_id"]}, {"$set": {"threat_category": result}})
    print(f"🔍 {doc['url']} → {result}")
