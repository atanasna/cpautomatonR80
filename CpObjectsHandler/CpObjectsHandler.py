from CpGroup import *
from CpHost import *
from CpNetwork import *
from CpRange import *

class CpObjectsHandler:
    def __init__(self):
        self.objects = list()

    # Accessors
    def hosts(self):
        all_matching_objects = filter(lambda obj: obj.__class__.__name__=="CpHost", self.objects)
        if all_matching_objects:
            return all_matching_objects
        else:
            return None
    def networks(self):
        all_matching_objects = filter(lambda obj: obj.__class__.__name__=="CpNetwork", self.objects)
        if all_matching_objects:
            return all_matching_objects
        else:
            return None
    def ranges(self):
        all_matching_objects = filter(lambda obj: obj.__class__.__name__=="CpRange", self.objects)
        if all_matching_objects:
            return all_matching_objects
        else:
            return None
    def groups(self):
        all_matching_objects = filter(lambda obj: obj.__class__.__name__=="CpGroup", self.objects)
        if all_matching_objects:
            return all_matching_objects
        else:
            return None

    # Seraches
    def find(self, name):
        all_matching_objects = filter(lambda obj: obj.name==name, self.objects)
        if all_matching_objects:
            return all_matching_objects[0]
        else:
            return None

    def load(self, json_input):
        # Load hosts
        for json_host in json_input["hosts"]:
            # check if required variable are presend in the input
            if "name" in json_host and "ipv4-address" in json_host:
                self.objects.append(CpHost(json_host["name"],json_host["ipv4-address"]))

        # Load networks
        for json_network in json_input["networks"]:
            # check if required variable are presend in the input
            if "name" in json_network and "subnet4" in json_network and "subnet-mask" in json_network:
                self.objects.append(CpNetwork(json_network["name"],json_network['subnet4']+"/"+json_network["subnet-mask"]))

        # Load ranges
        for json_range in json_input["ranges"]:
            # check if required variable are presend in the input
            if "name" in json_range and "ipv4-address-first" in json_range and "ipv4-address-last" in json_range:
                self.objects.append(CpRange(json_range["name"],json_range["ipv4-address-first"],json_range["ipv4-address-last"]))

        # Load Groups
        for json_group in json_input["groups"]:
            # check if required variable are presend in the input
            if "name" in json_group:
                self.objects.append(CpGroup(json_group["name"]))
        for json_group in json_input["groups"]:
            if "name" in json_group:
                group = self.find(json_group["name"])
            if "members" in json_group:
                for json_member in json_group["members"]:
                    member = self.find(json_member["name"])
                    if member:
                        print member.name
                        group.add(member)

    def print_objects(self):
        print("--------- Objects DB")
        print("===> Hosts")
        for host in self.hosts():
            print("    Name:" + host.name + " IP:" + host.address.exploded )
        print("===> Networks")
        for network in self.networks():
            print("    Name:" + network.name + " IP:" + network.address.exploded )
        print("===> Ranges")
        for range in self.ranges():
            print("    Name:" + range.name + " First-IP:" + range.first_address.exploded + " Last-IP:" + range.last_address.exploded)
        print("===> Groups")
        for group in self.groups():
            print("    Name:" + group.name)
            for member in group.expand():
                print("        Type:" + member.__class__.__name__ + " Name:" + member.name)
        print("---------")