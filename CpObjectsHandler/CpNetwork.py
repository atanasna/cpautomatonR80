from CpObject import *
import ipaddress

class CpNetwork(CpObject):
    # string: net_name
    # string: net_ip_address "10.10.0.0/16"
    # string: net_color
    def __init__(self, net_name, net_ip_address, net_color="Black"):
        CpObject.__init__(self, net_name, net_color)
        self.address = ipaddress.ip_network(net_ip_address)

    def broadcast(self):
        return self.address.broadcast_address