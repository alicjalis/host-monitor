import logging
import subprocess
import socket
import ssl
class BaseCheck:
    def __init__(self, host):
        self.host = host
        self.result = None

    def run(self) -> bool:
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


class TLSCheck(BaseCheck):
    def run(self)->bool:
        context = ssl.create_default_context()
        try:
            with socket.create_connection((self.host.address, 443), timeout=3) as sock:
                with context.wrap_socket(sock, server_hostname=self.host.address) as sock:
                    self.result = True
        except Exception as e:
            logging.error(f"TLS check failed {self.host.address}: {e}")
            self.result = False
        return self.result




