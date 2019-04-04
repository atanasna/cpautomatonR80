from CpNetworkObject import *
import ipaddress
import copy

class CpGroup(CpNetworkObject):
    # string: name
    # string: color
    def __init__(self, uid, name, color="Black"):
        CpNetworkObject.__init__(self, uid, name, color)
        self.__members = list()

    # CpObject Inherited: member
    def add(self,new_member):
        self.__members.append(new_member)

    # CpObject Inherited: member
    def remove(self,member):
        self.__members.remove(member)

    def members(self):
        return copy.deepcopy(self.__members)

    def expand(self):
        expanded_members = list()

        for el in list(self.__members):
            if el.__class__.__name__=="CpGroup":
                expanded_members += el.expand()
            else:
                expanded_members.append(el)

        return list(set(expanded_members))

    # NOT IMPLEMENTED
    def ip_include(self, obj):
        return False

    def ip_equal(self, obj):
        return False