from CpObject import *
import ipaddress

class CpHost(CpObject):
    # string: host_name
    # string: host_ip_address "10.10.10.10" 
    # string: host_color
    def __init__(self, host_name, host_ip_address, host_color="Black"):
        CpObject.__init__(self, host_name, host_color)
        self.address = ipaddress.ip_address(host_ip_address)

