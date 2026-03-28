from host import Host
from checks import PingCheck, PortCheck
from reporter import Reporter
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

host = Host(address="8.8.8.8", name="Google DNS")
ping = PingCheck(host)
ping.run()
port = PortCheck(host)
port.run()

reporter = Reporter([ping, port])
reporter.report()