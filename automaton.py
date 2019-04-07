from CpObjectsHandler.CpObjectsHandler import *
from CpObjectsHandler.CpNetwork import *
from CpApiHandler.CpApiHandler import *
from pprint import pprint
from dns import resolver,reversename
import json
import random

class Automaton:
    def __init__(self):
        self.__apiHandler = None
        self.__objectsHandler = None
        self.__policyHandler = None
        self.__config = None

        with open('config/config.json') as f:
            self.__config = json.load(f)

        self.__apiHandler = CpApiHandler(self.__config["api_credentials"]["address"], self.__config["api_credentials"]["username"], self.__config["api_credentials"]["password"])
        self.__objectsHandler = CpObjectsHandler()
        self.__objectsHandler.load(self.__apiHandler.get_net_objects())

    # The following method changes the color of all network objects based on the the setting under the __config/__config.json file @subnets and @color_mapping
    def colorize_objects(self):
        net_to_color_mapping = dict()
        for key in self.__config["subnets"]:
            for subnet in self.__config["subnets"][key]:
                net_to_color_mapping[CpNetwork("na",subnet,subnet)] = self.__config["color_mapping"][key]

        for obj in self.__objectsHandler.all_objects():
            for network in net_to_color_mapping:
                if network.ip_include(obj):
                    self.__objectsHandler.change_object_color(obj.uid,net_to_color_mapping[network])
                    self.__apiHandler.change_object_color(obj.uid,net_to_color_mapping[network])

    # The following method renames all host objects based on their IPs and dns reverse records using the DNS servers set in the __config/__config.json file @dns_servers
    def rename_objects_by_dns(self):
        dns_resolver = resolver.Resolver()
        dns_resolver.nameservers = self.__config["dns_servers"]

        for host in self.__objectsHandler.hosts():
            try:
                dns_name = str(dns_resolver.query(reversename.from_address(host.address.exploded),"PTR")[0])
                #print("Name for " + host.name + " is " + str(dns_name))
                if dns_name:
                    self.__objectsHandler.change_object_name(host.uid, dns_name)
                    self.__apiHandler.change_object_name(host.uid,dns_name)
            except:
                print("No record found for " + host.name + " with ip " + host.address.exploded)

    def delete_unused_objects(self):
        unused_objects = self.__apiHandler.get_unused_net_objects()
        pprint(unused_objects)
        if unused_objects:
            for object in unused_objects:
                print("Deleting: " + object["name"])
                self.__objectsHandler.delete_object(object["uid"])
                self.__apiHandler.delete_object(object["uid"])

    #def delete_duplicated_objects(self):

    def test(self):
        self.__objectsHandler.print_objects()
        #self.__apiHandler.push_sample_objects()
        #self.colorize_objects()
        #self.rename_objects_by_dns()
        #self.delete_unused_objects()
        #
        #for set in self.__objectsHandler.find_ip_duplicated_objects():
        #    pprint("------")
        #    for el in set:
        #        pprint(el.name)
        #
        self.__apiHandler.test_api_endpoint()
        #self.__objectsHandler.print_objects()

a = Automaton()
a.test()