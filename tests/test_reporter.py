import pytest

from src.checks import PingCheck
from src.host import Host
from src.reporter import Reporter


def test_reporter_logic():
    h = Host("8.8.8.8", "Google")
    check = PingCheck(h)
    check.result = True
    reporter = Reporter([check])
    assert reporter.checks[0].result is True
    assert reporter.checks[0].host.name == "Google"

from src.reporter import Reporter
def test_reporter_empty_list():
    reporter = Reporter([])
    try:
        reporter.report()
    except Exception as e:
        pytest.fail(f"Reporter failed with empty list: {e}")