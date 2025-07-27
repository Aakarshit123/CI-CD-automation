from flask import Flask, jsonify
from config import APP_CONFIG
from utils.logger import get_logs
import random, datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to FlaskApp AutoDeployer – Mini Dashboard API Version 2"
    })

@app.route('/health')
def health_check():
    return jsonify({"status": "Healthy", "timestamp": str(datetime.datetime.utcnow())})

@app.route('/api/users')
def get_users():
    users = [
        {"id": 1, "name": "Aakarshit", "role": "DevOps Engineer"},
        {"id": 2, "name": "sacchit", "role": "AI Engineer"}
    ]
    return jsonify(users)

@app.route('/api/metrics')
def get_metrics():
    metrics = {
        "cpu_usage": f"{random.randint(10, 90)}%",
        "memory_usage": f"{random.randint(1024, 8192)} MB",
        "active_containers": random.randint(1, 10),
        "last_updated": str(datetime.datetime.utcnow())
    }
    return jsonify(metrics)

@app.route('/api/logs')
def get_system_logs():
    logs = get_logs()
    return jsonify({"logs": logs})

@app.route('/api/config')
def get_config():
    return jsonify(APP_CONFIG)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
