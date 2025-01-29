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
    def test_routing_table(self):
        """Tests the presence of a specific route in the routing table."""
        routing_table = self.router.get_config(filter_='<ipv4-routing><routes/>')
        assert 'destination="10.1.1.0"' in str(routing_table)

    def test_bgp_neighbor(self):
        """Tests the presence of a BGP neighbor."""
        bgp_neighbors = self.router.get_config(filter_='<neighbors><neighbor><ip>10.1.2.2</ip></neighbor></neighbors>')
        assert 'remote-as' in str(bgp_neighbors)  # Basic check for BGP neighbor existence

    def test_ospf_process(self):
        """Tests the existence of an OSPF process."""
        ospf_config = self.router.get_config(filter_='<router><ospf><process-id>1</process-id></ospf></router>')
        assert '<process-id>1</process-id>' in str(ospf_config)

    def test_acl(self):
        """Tests the existence of an access-list."""
        acl_config = self.router.get_config(filter_='<ip-access-lists><access-list><name>ACL1</name></access-list></ip-access-lists>')
        assert '<name>ACL1</name>' in str(acl_config)


if __name__ == '__main__':
    pytest.main()