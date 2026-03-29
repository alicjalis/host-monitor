import time
import json
from host import Host
from checks import PingCheck, PortCheck
from reporter import Reporter
import logging

logging.basicConfig(
        filename='app.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def load_hosts_from_file(filename: str) -> list[Host]:
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [Host(h['address'], h['name'], h.get('port', 80)) for h in data]
    except Exception as e:
        logging.error(f"An unknown error occured while loading hosts: {e}")
        return []
    except json.decoder.JSONDecodeError:
        logging.error(f"A format  of a JSON file error occured")
        return []
    except FileNotFoundError:
        logging.error(f"File {filename} does not exist")
        return []

hosts_to_monitor = load_hosts_from_file('../hosts.json')
if not hosts_to_monitor:
    print("No hosts found")
    exit(1)

while True:
    try:
        for host in hosts_to_monitor:
            logging.info(f"Monitoring {host.name}")
            ping = PingCheck(host)
            ping.run()
            port = PortCheck(host)
            port.run()
            reporter = Reporter([ping, port])
            reporter.report()

        time.sleep(3)
    except (KeyboardInterrupt, SystemExit):
        print("\nGoodbye!")
        break