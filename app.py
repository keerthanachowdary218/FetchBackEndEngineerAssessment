import uuid
from flask import Flask, request, jsonify
from utils import calculate_points

app = Flask(__name__)
receipts_db = {}

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    receipt = request.get_json()
    # Validate receipt fields
    required_fields = ['retailer', 'purchaseDate', 'purchaseTime', 'items', 'total']
    if not all(field in receipt for field in required_fields):
        return jsonify({'error': 'The receipt is invalid. Please verify input.'}), 400
    receipt_id = str(uuid.uuid4())
    points = calculate_points(receipt)
    receipts_db[receipt_id] = points
    return jsonify({'id': receipt_id}), 200

@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
    points = receipts_db.get(receipt_id)
    if points is None:
        return jsonify({'error': 'No receipt found for that ID.'}), 404
    return jsonify({'points': points}), 200

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
