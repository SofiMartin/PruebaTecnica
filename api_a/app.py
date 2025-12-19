from flask import Flask, request, jsonify
from datetime import datetime
import requests

app = Flask(__name__)

API_B_URL = 'http://api_b:5001'

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        'status': 'active',
        'service': 'API A',
        'timestamp': datetime.utcnow().isoformat()
    }), 200

@app.route('/request-process', methods=['POST'])
def request_process():
    try:
        data = request.get_json()
        
        if not data or 'value' not in data:
            return jsonify({
                'error': 'Missing required field: value'
            }), 400
        
        try:
            response = requests.post(
                f'{API_B_URL}/process',
                json=data,
                timeout=10
            )
            
            if response.status_code != 200:
                return jsonify({
                    'error': 'API B returned an error',
                    'status_code': response.status_code,
                    'details': response.json() if response.text else 'No details'
                }), 502
            
            api_b_response = response.json()
            
            final_response = {
                'original_data': data,
                'api_b_response': api_b_response,
                'message': 'procesado correctamente',
                'timestamp': datetime.utcnow().isoformat()
            }
            
            return jsonify(final_response), 200
            
        except requests.exceptions.ConnectionError:
            return jsonify({
                'error': 'Cannot connect to API B',
                'details': 'API B is not available or not responding'
            }), 502
            
        except requests.exceptions.Timeout:
            return jsonify({
                'error': 'API B request timeout',
                'details': 'API B took too long to respond'
            }), 502
            
        except requests.exceptions.RequestException as e:
            return jsonify({
                'error': 'Error communicating with API B',
                'details': str(e)
            }), 502
            
    except Exception as e:
        return jsonify({
            'error': 'Internal server error',
            'details': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
