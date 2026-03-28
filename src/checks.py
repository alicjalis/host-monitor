import logging
import subprocess
import socket
class BaseCheck:
    def __init__(self, host):
        self.host = host
        self.result = None

    def run(self):
        raise NotImplementedError


class PingCheck(BaseCheck):
    def run(self):
        try:
            result = subprocess.run(
                ["ping", "-c", "1", "-W", "1",self.host.address],
                capture_output=True
            )
            self.result = (result.returncode == 0)

        except (OSError, ValueError):
            logging.error(f"Ping check failed {self.host.address}")
            self.result = False
        return self.result


class PortCheck(BaseCheck):
    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            result = s.connect_ex((self.host.address, self.host.port))
            self.result = result == 0
        except socket.gaierror:
            logging.error(f"Port check failed {self.host.port, self.host.address}")
            self.result = False
        finally:
            s.close()
        return self.result




