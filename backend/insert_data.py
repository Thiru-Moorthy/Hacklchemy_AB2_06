import pandas as pd
import pymongo

# ✅ Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["darkweb"]  # Database Name
collection = db["threat_data"]  # Collection Name
client = pymongo.MongoClient("mongodb://localhost:27017/")


# ✅ Read CSV File
csv_file = r"D:\dark_web_intelligence\backend\datasets\cybersecurity_large_synthesized_data.csv" # Change this path
df = pd.read_csv(csv_file)

# ✅ Convert DataFrame to Dictionary and Insert into MongoDB
data = df.to_dict(orient="records")  # Convert rows into dictionary format
collection.insert_many(data)

print("✅ Data successfully inserted into MongoDB!")

