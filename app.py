from flask import Flask, jsonify

application = Flask(__name__)

@application.route('/')
def home():
    return jsonify({
        "service_name": "CloudKart Core Engine",
        "system_status": "UP"
    }), 200

@application.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "database_connection": "active"
    }), 200

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
