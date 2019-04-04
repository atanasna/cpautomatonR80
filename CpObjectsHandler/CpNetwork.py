from CpNetworkObject import *
import ipaddress

class CpNetwork(CpNetworkObject):
    # string: name
    # string: net_address "10.10.0.0/16"
    # string: color
    def __init__(self, uid, name, net_address, color="Black"):
        CpObject.__init__(self, uid, name, color)
        self.address = ipaddress.ip_network(net_address)

    def ip_include(self, obj):
        if obj.__class__.__name__ == "CpHost":
            return obj.address in self.address
        elif obj.__class__.__name__ == "CpNetwork":
            return obj.address.subnet_of(self.address)
        elif obj.__class__.__name__ == "CpRange":
            return obj.first_address in self.address and obj.last_address in self.address
        elif obj.__class__.__name__ == "CpGroup":
            if obj.expand():
                for group_el in obj.expand():
                    if self.ip_include(group_el):
                        continue
                    else:
                        return False
                return True
            else:
                return False
        else:
            return False

    def ip_equal(self,obj):
        if obj.__class__.__name__ == "CpHost":
            return self.address.network_address == obj.address and self.address.broadcast_address == obj.address 
        elif obj.__class__.__name__ == "CpNetwork":
            return self.address == obj.address
        elif obj.__class__.__name__ == "CpRange":
            return self.address.network_address == obj.first_address and self.address.broadcast_address == obj.last_address
        else:
            return False