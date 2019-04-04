from CpNetworkObject import *
import ipaddress

class CpRange(CpNetworkObject):
    # string: name
    # string: first_ip_address "10.10.10.10"
    # string: last_ip_address "10.10.10.244"
    # string: color
    def __init__(self, uid, name, first_ip_address, last_ip_address, color="Black"):
        CpObject.__init__(self, uid, name, color)
        self.first_address = ipaddress.ip_address(first_ip_address)
        self.last_address = ipaddress.ip_address(last_ip_address)

    def ip_include(self, obj):
        if obj.__class__.__name__ == "CpHost":
            return self.first_address <= obj.address <= self.last_address
        elif obj.__class__.__name__ == "CpNetwork":
            return self.first_address <= obj.address.network_address and obj.address.broadcast_address <= self.last_address
        elif obj.__class__.__name__ == "CpRange":
            return self.first_address <= obj.first_address and obj.last_address <= self.last_address
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
            return self.first_address == obj.address and self.last_address == obj.address
        elif obj.__class__.__name__ == "CpNetwork":
            return self.first_address == obj.address.network_address and self.last_address == obj.address.broadcast_address 
        elif obj.__class__.__name__ == "CpRange":
            return self.first_address == obj.first_address and self.last_address == obj.last_address
        else:
            return False