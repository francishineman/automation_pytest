#!/usr/bin/env/python3

import pytest
from netmiko import ConnectHandler

# Replace with your actual device credentials
DEVICE = {
    'device_type': 'cisco_ios',
    'host': '192.168.100.123',
    'username': 'cisco_dev_username',
    'password': 'cisco_dev_password',
}

@pytest.fixture(scope="module")
def net_connect():
    """Establish a connection to the Cisco router."""
    try:
        net_connect = ConnectHandler(**DEVICE)
        yield net_connect
    finally:
        net_connect.disconnect()

def test_ping(net_connect):
    """Test ping to a specific IP address."""
    output = net_connect.send_command("ping 8.8.8.8")
    assert "Success rate is 100 percent" in output

def test_interface_status(net_connect):
    """Test interface status of a specific interface."""
    output = net_connect.send_command("show interfaces GigabitEthernet0/1 status")
    assert "Protocol is up" in output

def test_bgp_neighbors(net_connect):
    """Test BGP neighbor status."""
    output = net_connect.send_command("show ip bgp neighbors")
    assert "192.168.1.2" in output  # Replace with the expected neighbor IP


# Test execution.
if __name__ == "__main__":
    pytest.main()
