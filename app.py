import threading
from flask import Flask, jsonify
from src.monitor import load_hosts_from_file, monitoring_loop
import logging

app = Flask(__name__)
logging.basicConfig(
        filename='app.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

hosts_to_monitor = load_hosts_from_file("hosts.json")
thread = threading.Thread(target=monitoring_loop, args=(hosts_to_monitor,), daemon=True)
thread.start()

@app.route('/')
def home():
    return "API!"

@app.route('/api/hosts', methods=['GET'])
def get_hosts():
    result = []
    for host in hosts_to_monitor:
        result.append({
            "name": host.name,
            "address": host.address,
            "is_alive": host.is_alive,
            "last_checked": str(host.last_checked)
        })
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False)