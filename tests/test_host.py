from src.host import Host

def test_host_initialization():
    h = Host("8.8.8.8", "Google")
    assert h.address == "8.8.8.8"
    