import logging
from src.monitor import load_hosts_from_file, monitoring_loop

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    hosts = load_hosts_from_file('hosts.json')
    if not hosts:
        print("No hosts found")
        exit(1)
    monitoring_loop(hosts)