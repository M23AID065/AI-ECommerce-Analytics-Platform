
from flask import Flask, jsonify, request
from api.customer import segment_customers
from api.fraud import detect_fraud
from api.insights import get_forecasts

app = Flask(__name__)

@app.route('/api/v1/customer-segmentation', methods=['POST'])
def customer_segmentation():
    data = request.get_json()
    result = segment_customers(data)
    return jsonify(result)

@app.route('/api/v1/fraud-detection', methods=['POST'])
def fraud_detection():
    data = request.get_json()
    result = detect_fraud(data)
    return jsonify(result)

@app.route('/api/v1/demand-forecast', methods=['GET'])
def demand_forecast():
    result = get_forecasts()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
