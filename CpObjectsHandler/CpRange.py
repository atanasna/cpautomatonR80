from CpObject import *
import ipaddress

class CpRange(CpObject):
    # string: range_name
    # string: first_ip_address "10.10.10.10"
    # string: last_ip_address "10.10.10.244"
    # string: range_color
    def __init__(self, range_name, first_ip_address, last_ip_address, range_color="Black"):
        CpObject.__init__(self, range_name, range_color)
        self.first_address = ipaddress.ip_address(first_ip_address)
        self.last_address = ipaddress.ip_address(last_ip_address)
