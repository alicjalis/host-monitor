from unittest.mock import patch, MagicMock

from src.checks import PingCheck, TLSCheck, PortCheck
from src.host import Host

def test_tls_check_invalid_host():
    h = Host("this.is.not.a.host", "Fake Host", 443)
    check = TLSCheck(h)
    result = check.run()
    assert result is False
    assert check.result is False

def test_tls_check_success():
    h = Host("google.com", "Google", 443)
    check = TLSCheck(h)
    with patch("src.checks.socket.create_connection") as mock_connect:
        with patch("src.checks.ssl.create_default_context") as mock_context:
            result = check.run()
    assert result is True

def test_ping_check_success():
    h = Host("8.8.8.8", "Google")
    check = PingCheck(h)
    with patch("src.checks.subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0)
        result = check.run()
    assert result is True

def test_ping_check_failure():
    h = Host("8.8.8.8", "Google")
    check = PingCheck(h)
    with patch("src.checks.subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=1)
        result = check.run()
    assert result is False

def test_port_check_invalid_ip():
    h = Host("999.999.999.999", "Fake", 80)
    check = PortCheck(h)
    assert check.run() is False

def test_port_check_exception():
    h = Host("invalid.address", "Fake", 80)
    check = PortCheck(h)
    with patch("src.checks.socket.socket.connect_ex", side_effect=Exception("Connection error")):
        result = check.run()
    assert result is False