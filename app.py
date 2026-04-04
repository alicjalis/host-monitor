import threading
import time
from flask import Flask, jsonify
from src.host import Host
from src.checks import PingCheck, PortCheck, TLSCheck
from src.reporter import Reporter
from main import load_hosts_from_file
import logging

app = Flask(__name__)
logging.basicConfig(
        filename='app.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

hosts_to_monitor = load_hosts_from_file("hosts.json")
def monitoring_loop():
    while True:
        try:
            for host in hosts_to_monitor:
                logging.info(f"Monitoring {host.name}")
                ping = PingCheck(host)
                ping.run()
                port = PortCheck(host)
                port.run()
                tls = TLSCheck(host)
                tls.run()
                host.update_status(ping.result)
                reporter = Reporter([ping, port, tls])
                reporter.report()

            time.sleep(3)
        except (KeyboardInterrupt, SystemExit):
            print("\nGoodbye!")
            break

thread = threading.Thread(target=monitoring_loop, daemon=True)
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