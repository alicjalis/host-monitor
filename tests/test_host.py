from src.checks import PingCheck, TLSCheck
from src.host import Host
from src.reporter import Reporter


def test_host_initialization():
    h = Host("8.8.8.8", "Google")
    assert h.address == "8.8.8.8"




