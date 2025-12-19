from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        'status': 'active',
        'service': 'API B',
        'timestamp': datetime.utcnow().isoformat()
    }), 200

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.get_json()
        
        if not data or 'value' not in data:
            return jsonify({
                'error': 'Missing required field: value'
            }), 400
        
        value = data['value']
        
        if isinstance(value, (int, float)):
            processed_result = value * 2
        elif isinstance(value, str):
            processed_result = len(value)
        else:
            return jsonify({
                'error': 'Invalid value type. Expected number or string'
            }), 400
        
        response = {
            'original_value': value,
            'processed_result': processed_result,
            'request_id': str(uuid.uuid4()),
            'timestamp': datetime.utcnow().isoformat()
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Internal server error',
            'details': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
