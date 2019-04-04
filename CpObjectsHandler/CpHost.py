from CpNetworkObject import *
import ipaddress

class CpHost(CpNetworkObject):
    # string: name
    # string: ip_address "10.10.10.10" 
    # string: color
    def __init__(self, uid, name, ip_address, color="Black"):
        CpNetworkObject.__init__(self, uid, name, color)
        self.address = ipaddress.ip_address(ip_address)

    def ip_include(self, obj):
        return False

    def ip_equal(self,obj):
        if obj.__class__.__name__ == "CpHost":
            return self.address == obj.address
        elif obj.__class__.__name__ == "CpNetwork":
            return self.address == obj.address.network_address and self.address == obj.address.broadcast_address
        elif obj.__class__.__name__ == "CpRange":
            return self.address == obj.first_address and self.address == obj.last_address
        else:
            return False