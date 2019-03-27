from CpObject import *
import ipaddress

class CpGroup(CpObject):
    # string: group_name
    # string: group_color
    def __init__(self, group_name, group_color="Black"):
        CpObject.__init__(self, group_name, group_color)
        self.members = list()

    # CpObject Inherited: member
    def add(self,new_member):
        self.members.append(new_member)

    # CpObject Inherited: member
    def remove(self,member):
        self.members.remove(member)

    # CpObject Inherited: member
    def expand(self):
        expanded_members = list()

        for el in list(self.members):
            if el.__class__.__name__=="CpGroup":
                expanded_members += el.expand()
            else:
                expanded_members.append(el)

        return list(set(expanded_members))