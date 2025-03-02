# Dark Web Intelligence

## 📌 Overview
Dark Web Intelligence is a system that crawls the dark web, applies NLP-based threat analysis, and visualizes hacker networks using graph analysis. The project includes a backend API and a frontend interface.

## 🚀 Features
- **Dark Web Crawler**: Extracts data from .onion sites.
- **NLP Analysis**: Performs threat classification and named entity recognition (NER).
- **Graph Intelligence**: Maps connections between hacker entities.
- **Flask Backend**: Provides an API to access data.
- **React Frontend**: Displays insights in a user-friendly way.

## 🛠 Installation

### **1️⃣ Install Dependencies**
Make sure you have **Python 3.10+**, **Node.js**, and **Tor** installed.

#### 📌 **Install Python Dependencies**
```bash
pip install -r requirements.txt
```

#### 📌 **Install Node.js Dependencies**
```bash
cd frontend
npm install
```

### **2️⃣ Install and Start Tor**
The crawler requires the **Tor Expert Bundle**.

#### **🔹 Linux / macOS**
Install Tor:
```bash
sudo apt install tor  # Ubuntu/Debian
brew install tor      # macOS
```
Start Tor:
```bash
tor
```

#### **🔹 Windows**
1. Download the **Tor Expert Bundle** from [Tor Project](https://www.torproject.org/download/).
2. Extract the files to `C:\Tor`.
3. Open **Command Prompt** and run:
```bash
   cd C:\Tor
   tor.exe
```
   Keep this **running in the background**.

## 📲 Running the Pipeline

### **Step 1: Run the Dark Web Crawler**
```bash
python crawler/tor_crawler.py
```

### **Step 2: Run NLP Analysis**
```bash
python nlp_analysis/threat_classifier.py
python nlp_analysis/named_entity_recognition.py
```

### **Step 3: Run Graph Intelligence**
```bash
python graph_analysis/hacker_graph.py
```

### **Step 4: Start the Backend API**
```bash
python backend/app.py
```

### **Step 5: Start the Frontend**
```bash
cd frontend
npm start
```
Open **http://localhost:3000** in your browser.

## 🛠 Troubleshooting

### ❌ **Tor Connection Error**
**Error**: `[WinError 10061] No connection could be made because the target machine actively refused it`

**Fix**: Ensure Tor is running by executing:
```bash
tor
```
If it’s not recognized, navigate to `C:\Tor` and run `tor.exe`.

## 🏰 Future Enhancements
- 🔹 Improve threat detection using LLMs.
- 🔹 Optimize the crawler for deeper penetration.
- 🔹 Add real-time threat monitoring.

## 👨‍💻 Contributors
- Thirumoorthy R(Project Lead)


