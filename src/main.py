from host import Host
from checks import PingCheck, PortCheck
from reporter import Reporter

host = Host(address="8.8.8.8", name="Google DNS")
ping = PingCheck(host)
ping.run()
port = PortCheck(host)
port.run()

reporter = Reporter([ping, port])
reporter.report()