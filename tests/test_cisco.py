import pytest
from framework.cisco import CiscoDevice
import logging

logger = logging.getLogger(__name__)

@pytest.fixture(scope="module")
def device():
    device = CiscoDevice(
        host='<your_device_ip>',
        username='<your_username>',
        password='<your_password>',
        logger=logger
    )
    device.connect()
    yield device
    device.disconnect()

def test_get_uptime(device):
    uptime = device.get_uptime()
    assert uptime is not None

def test_get_vlan_info(device):
    vlan_info = device.get_vlan_info()
    assert vlan_info is not None

def test_get_ospf_neighbors(device):
    ospf_neighbors = device.get_ospf_neighbors()
    assert ospf_neighbors is not None

def test_get_bgp_neighbors(device):
    bgp_neighbors = device.get_bgp_neighbors()
    assert bgp_neighbors is not None

def test_get_spanning_tree_info(device):
    spanning_tree_info = device.get_spanning_tree_info()
    assert spanning_tree_info is not None

def test_get_etherchannel_info(device):
    etherchannel_info = device.get_etherchannel_info()
    assert etherchannel_info is not None

def test_get_qos_policy_info(device):
    qos_policy_info = device.get_qos_policy_info()
    assert qos_policy_info is not None

def test_get_acl_info(device):
    acl_info = device.get_acl_info()
    assert acl_info is not None

def test_get_port_security_info(device):
    port_security_info = device.get_port_security_info()
    assert port_security_info is not None

def test_get_cpu_utilization(device):
    cpu_utilization = device.get_cpu_utilization()
    assert cpu_utilization is not None

def test_get_memory_utilization(device):
    memory_utilization = device.get_memory_utilization()
    assert memory_utilization is not None

def test_get_interface_errors(device):
    interface_errors = device.get_interface_errors()
    assert interface_errors is not None