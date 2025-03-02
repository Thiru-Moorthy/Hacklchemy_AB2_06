import networkx as nx
import matplotlib.pyplot as plt
import pymongo

# Load MongoDB Data
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["darkweb"]
collection = db["threat_data"]

# Create Graph
G = nx.Graph()

# Build Hacker Connection Graph
for doc in collection.find():
    if "threat_category" in doc:
        G.add_edge(doc["url"], doc["threat_category"][0]["label"])

# Visualize Graph
plt.figure(figsize=(10, 6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', font_size=10)
plt.show()
