from .device import Device

class CiscoDevice(Device):
    """
    Class for Cisco devices.
    """
    def __init__(self, host, username, password, logger):
        super().__init__(host, username, password, 'cisco_ios', logger)

    def get_uptime(self):
        """
        Get uptime of the device.
        """
        output = self.send_command("show uptime")
        return output

    def get_vlan_info(self):
        """
        Get VLAN information.
        """
        output = self.send_command("show vlan brief")
        return output

    def get_ospf_neighbors(self):
        """
        Get OSPF neighbor information.
        """
        output = self.send_command("show ip ospf neighbor")
        return output

    def get_bgp_neighbors(self):
        """
        Get BGP neighbor information.
        """
        output = self.send_command("show ip bgp summary")
        return output

    def get_spanning_tree_info(self):
        """
        Get Spanning Tree Protocol information.
        """
        output = self.send_command("show spanning-tree")
        return output

    def get_etherchannel_info(self):
        """
        Get EtherChannel information.
        """
        output = self.send_command("show etherchannel summary")
        return output

    def get_qos_policy_info(self):
        """
        Get QoS policy information.
        """
        output = self.send_command("show policy-map")
        return output

    def get_acl_info(self):
        """
        Get ACL information.
        """
        output = self.send_command("show access-lists")
        return output

    def get_port_security_info(self):
        """
        Get port security information.
        """
        output = self.send_command("show interface status | include Port Security")
        return output

    def get_cpu_utilization(self):
        """
        Get CPU utilization.
        """
        output = self.send_command("show processes cpu sorted | include CPU utilization")
        return output

    def get_memory_utilization(self):
        """
        Get memory utilization.
        """
        output = self.send_command("show memory summary")
        return output

    def get_interface_errors(self):
        """
        Get interface errors.
        """
        output = self.send_command("show interfaces status | include errors")
        return output
