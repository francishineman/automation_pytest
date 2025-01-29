from netmiko import ConnectHandler
import logging

class Device:
    """
    Base class for network devices.
    """
    def __init__(self, host, username, password, device_type, logger):
        self.host = host
        self.username = username
        self.password = password
        self.device_type = device_type
        self.logger = logger

    def connect(self):
        """
        Establish a connection to the device.
        """
        try:
            self.net_connect = ConnectHandler(
                device_type=self.device_type,
                ip=self.host,
                username=self.username,
                password=self.password
            )
            self.logger.info(f"Connected to {self.host}")
        except Exception as e:
            self.logger.error(f"Failed to connect to {self.host}: {e}")
            raise

    def disconnect(self):
        """
        Close the connection to the device.
        """
        try:
            self.net_connect.disconnect()
            self.logger.info(f"Disconnected from {self.host}")
        except Exception as e:
            self.logger.error(f"Failed to disconnect from {self.host}: {e}")

    def send_command(self, command):
        """
        Send a command to the device and return the output.
        """
        try:
            output = self.net_connect.send_command(command)
            return output
        except Exception as e:
            self.logger.error(f"Failed to send command to {self.host}: {e}")
            return None
