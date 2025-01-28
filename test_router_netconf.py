import pytest
from ncclient import manager
from lxml import etree

# Replace with your actual device credentials
HOST = '192.168.100.222'
PORT = 22
USER = 'cisco_username'
PASS = 'cisco_password'

class CiscoRouter:
    """
    Class to represent a Cisco router and provide methods for Netconf interactions.
    """

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.conn = None

    def connect(self):
        """Connects to the Cisco device using Netconf."""
        try:
            self.conn = manager.connect(
                host=self.host,
                port=self.port,
                username=self.username,
                password=self.password,
                hostkey_verify=False,
                device_params={'name': 'ios'}
            )
        except Exception as e:
            pytest.fail(f"Failed to connect to device: {e}")

    def close_connection(self):
        """Closes the Netconf connection."""
        try:
            if self.conn:
                self.conn.close_session()
        except Exception as e:
            pytest.fail(f"Failed to close connection: {e}")

    def get_config(self, filter_='all'):
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
            result = self.conn.dispatch(etree.fromstring(rpc))
            return result
        except Exception as e:
            pytest.fail(f"Failed to get configuration: {e}")

class TestCiscoRouterFeatures:
    """
    Test class for Cisco router features.
    """

    def setup_class(self):
        """Sets up the connection to the device before each test."""
        self.router = CiscoRouter(HOST, PORT, USER, PASS)
        self.router.connect()

    def teardown_class(self):
        """Closes the connection to the device after each test."""
        self.router.close_connection()

    def test_interface_status(self):
        """Tests the status of a specific interface."""
        interface_status = self.router.get_config(filter_='<interfaces><interface name="GigabitEthernet0/0"/>')
        assert 'oper-status="up"' in str(interface_status)

if __name__ == '__main__':
    pytest.main()