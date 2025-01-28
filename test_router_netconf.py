import pytest
from ncclient import manager
from lxml import etree

# Replace with your actual device credentials
HOST = '192.168.1.1'
PORT = 22
USER = 'cisco'
PASS = 'cisco'

# Define reusable functions for common operations
def connect_to_device():
    """Connects to the Cisco device using Netconf."""
    try:
        conn = manager.connect(
            host=HOST,
            port=PORT,
            username=USER,
            password=PASS,
            hostkey_verify=False,
            device_params={'name': 'ios'}
        )
        return conn
    except Exception as e:
        pytest.fail(f"Failed to connect to device: {e}")

def close_connection(conn):
    """Closes the Netconf connection."""
    try:
        conn.close_session()
    except Exception as e:
        pytest.fail(f"Failed to close connection: {e}")

def get_config(conn, filter_='all'):
    """Retrieves the current configuration from the device."""
    try:
        rpc = """
        <get-config>
          <source>
            <running/>
          </source>
          <filter type='subtree'>
            {filter_}
          </filter>
        </get-config>
        """.format(filter_=filter_)
        result = conn.dispatch(etree.fromstring(rpc))
        return result
    except Exception as e:
        pytest.fail(f"Failed to get configuration: {e}")

def compare_configs(expected, actual):
    """Compares two configurations and returns True if they match."""
    try:
        # Use a more robust comparison method (e.g., difflib) for real-world scenarios
        return expected == actual
    except Exception as e:
        pytest.fail(f"Failed to compare configurations: {e}")

# Define test cases for specific router features
def test_interface_status():
    """Tests the status of a specific interface."""
    conn = connect_to_device()
    try:
        # Get the interface status using Netconf
        interface_status = get_config(conn, filter_='<interfaces><interface name="GigabitEthernet0/0"/>')
        # Assert that the interface is up
        assert 'oper-status="up"' in str(interface_status)
    finally:
        close_connection(conn)

def test_routing_table():
    """Tests the presence of a specific route in the routing table."""
    conn = connect_to_device()
    try:
        # Get the routing table using Netconf
        routing_table = get_config(conn, filter_='<ipv4-routing><routes/>')
        # Assert that the expected route exists
        assert 'destination="10.1.1.0"' in str(routing_table)
    finally:
        close_connection(conn)

# Add more test cases for other router features (e.g., BGP, OSPF, ACLs)

if __name__ == '__main__':
    pytest.main()
