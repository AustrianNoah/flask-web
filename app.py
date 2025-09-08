from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy", "message": "Flask app is running!"})

@app.route('/api/data')
def get_data():
    sample_data = {
        "users": ["Alice", "Bob", "Charlie"],
        "timestamp": "2024-01-15T10:30:00Z"
    }
    return jsonify(sample_data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)