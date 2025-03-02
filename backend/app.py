from flask import Flask, jsonify
from database import collection

app = Flask(__name__)

# API Endpoint for Threat Data
@app.route('/threats', methods=['GET'])
def get_threats():
    threats = list(collection.find({}, {"_id": 0}))
    return jsonify(threats)

if __name__ == '__main__':
    app.run(debug=True)
