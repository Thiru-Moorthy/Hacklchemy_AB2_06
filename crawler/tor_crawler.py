import requests
from bs4 import BeautifulSoup
import pymongo
from proxy_manager import renew_tor_ip

# TOR Proxy Settings
PROXIES = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050",
}

# MongoDB Setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["darkweb"]
collection = db["threat_data"]

# Function to Scrape Dark Web
def scrape_dark_web(url):
    try:
        response = requests.get(url, proxies=PROXIES, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            data = soup.get_text()
            collection.insert_one({"url": url, "data": data})
            print(f"✅ Data saved from {url}")
        else:
            print(f"❌ Error {response.status_code}: Could not access {url}")
    except Exception as e:
        print(f"❌ Failed: {e}")

# Run Scraper
dark_web_sites = [
    "http://exampledarkweb.onion",
    "http://hackerforum.onion"
]

renew_tor_ip()
for url in dark_web_sites:
    scrape_dark_web(url)
