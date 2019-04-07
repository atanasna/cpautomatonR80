from pprint import pprint
from CpGroup import *
from CpHost import *
from CpNetwork import *
from CpRange import *
import copy

# The objects can obly by modified using the Modifing Methods
class CpObjectsHandler:
    def __init__(self):
        self.__objects = list()

    # Accessors
    def __hosts(self):
        all_matching_objects = filter(lambda obj: obj.__class__.__name__=="CpHost", self.__objects)
        if all_matching_objects:
            return all_matching_objects
        else:
            return None
    def __networks(self):
        all_matching_objects = filter(lambda obj: obj.__class__.__name__=="CpNetwork", self.__objects)
        if all_matching_objects:
            return all_matching_objects
        else:
            return None
    def __ranges(self):
        all_matching_objects = filter(lambda obj: obj.__class__.__name__=="CpRange", self.__objects)
        if all_matching_objects:
            return all_matching_objects
        else:
            return None
    def __groups(self):
        all_matching_objects = filter(lambda obj: obj.__class__.__name__=="CpGroup", self.__objects)
        if all_matching_objects:
            return all_matching_objects
        else:
            return None
    def __find_by_uid(self, uid):
        all_matching_objects = filter(lambda obj: obj.uid==uid, self.__objects)
        if all_matching_objects:
            return all_matching_objects[0]
        else:
            return None
    def __find_by_name(self, name):
        all_matching_objects = filter(lambda obj: obj.name==name, self.__objects)
        if all_matching_objects:
            return all_matching_objects[0]
        else:
            return None

    #   All public accessors return copies of the objects and not the actual objects
    def all_objects(self):
        return copy.deepcopy(self.__objects)
    def hosts(self):
        return copy.deepcopy(self.__hosts())
    def networks(self):
        return copy.deepcopy(self.__networks())
    def ranges(self):
        return copy.deepcopy(self.__ranges())
    def groups(self):
        return copy.deepcopy(self.__groups())
    def find_by_uid(self, uid):
        return copy.deepcopy(self.__find_by_uid(uid))
    def find_by_name(self, name):
        return copy.deepcopy(self.__find_by_name(name))
    def find_ip_duplicated_objects(self):
        duplicated_sets = list()
        for focus_obj in self.__objects:
            duplicated_set = [focus_obj]
            for compared_obj in self.__objects:
                if focus_obj == compared_obj:
                    continue
                else:
                    if focus_obj.ip_equal(compared_obj):
                        duplicated_set.append(compared_obj)
            if len(duplicated_set) > 1:
                duplicated_sets.append(sorted(duplicated_set))

        # sort and get uniques only
        uniq_duplicated_sets = list()
        for set in duplicated_sets:
            if set in uniq_duplicated_sets:
                continue
            else:
                uniq_duplicated_sets.append(set)

        return copy.deepcopy(uniq_duplicated_sets)

    #Modifiers
    def change_object_color(self, uid, new_color):
        obj = self.__find_by_uid(uid)
        if obj:
            obj.color = new_color
            return True
        else:
            return False
    def change_object_name(self, uid, new_name):
        obj = self.__find_by_uid(uid)
        if obj:
            obj.name = new_name
            return True
        else:
            return False
    def delete_object(self, uid):
        deleted_obj = self.__find_by_uid(uid) 
        self.__objects.remove(deleted_obj)

        for group in self.__groups():
            if deleted_obj in group.members():
                group.remove(deleted_obj)

    #Misc
    def load(self, json_input):
        # Load hosts
        for json_host in json_input["hosts"]:
            # check if required variable are presend in the input
            if "uid" in json_host and "name" in json_host and "ipv4-address" in json_host:
                self.__objects.append(CpHost(json_host["uid"], json_host["name"],json_host["ipv4-address"]))

        # Load networks
        for json_network in json_input["networks"]:
            # check if required variable are presend in the input
            if "uid" in json_network and "name" in json_network and "subnet4" in json_network and "subnet-mask" in json_network:
                self.__objects.append(CpNetwork(json_network["uid"], json_network["name"],json_network['subnet4']+"/"+json_network["subnet-mask"]))

        # Load ranges
        for json_range in json_input["ranges"]:
            # check if required variable are presend in the input
            if "uid" in json_range and "name" in json_range and "ipv4-address-first" in json_range and "ipv4-address-last" in json_range:
                self.__objects.append(CpRange(json_range["uid"], json_range["name"],json_range["ipv4-address-first"],json_range["ipv4-address-last"]))

        # Load Groups
        for json_group in json_input["groups"]:
            # check if required variable are presend in the input
            if "uid" in json_group and "name" in json_group:
                self.__objects.append(CpGroup(json_group["uid"], json_group["name"]))
        for json_group in json_input["groups"]:
            if "name" in json_group:
                group = self.__find_by_name(json_group["name"])
            if "members" in json_group:
                for json_member in json_group["members"]:
                    member = self.__find_by_name(json_member["name"])
                    if member:
                        group.add(member)
    def print_objects(self):
        print("--------- Objects DB")
        print("===> Hosts")
        for host in self.hosts():
            print("    Name:" + host.name + " Color:" + host.color + " IP:" + host.address.exploded + " UID:" + host.uid)
        print("===> Networks")
        for network in self.networks():
            print("    Name:" + network.name + " Color:" + network.color + " IP:" + network.address.exploded )
        print("===> Ranges")
        for range in self.ranges():
            print("    Name:" + range.name + " Color:" + range.color + " First-IP:" + range.first_address.exploded + " Last-IP:" + range.last_address.exploded)
        print("===> Groups")
        for group in self.groups():
            print("    Name:" + group.name + " Color:" + group.color)
            for member in group.expand():
                print("        Type:" + member.__class__.__name__ + " Name:" + member.name)
        print("---------")