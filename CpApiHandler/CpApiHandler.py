import requests
import json
from pprint import pprint
from CpApiConnector import *
# defining the api-endpoint  

class CpApiHandler:
    def __init__(self, server_ip, user, password):
        self.__api_connector = CpApiConnector("https://"+server_ip+"/web_api")
        self.__user = user
        self.__password = password

    # Object Getters
    def get_net_objects(self):
        if not self.__api_connector.login(self.__user,self.__password):
            return None
     
        objects = dict()
        objects["hosts"] = list()
        objects["networks"] = list()
        objects["ranges"] = list()
        objects["groups"] = list()
        for host in self.__api_connector.get_all_hosts()["objects"]:
            objects["hosts"].append(self.__api_connector.get_host(host["uid"]))
        for network in self.__api_connector.get_all_networks()["objects"]:
            objects["networks"].append(self.__api_connector.get_network(network["uid"]))
        for range in self.__api_connector.get_all_ranges()["objects"]:
            objects["ranges"].append(self.__api_connector.get_range(range["uid"]))
        for group in self.__api_connector.get_all_groups()["objects"]:
            objects["groups"].append(self.__api_connector.get_group(group["uid"]))

        self.__api_connector.logout()
        return objects
    def get_unused_net_objects(self):
        if not self.__api_connector.login(self.__user,self.__password):
            return None
     
        unused_objects = list()

        for object in self.__api_connector.get_unused_objects()["objects"]:
            if object["type"] == "host":
                unused_objects.append(self.__api_connector.get_host(object["uid"]))
            elif object["type"] == "network":
                unused_objects.append(self.__api_connector.get_network(object["uid"]))
            elif object["type"] == "address-range":
                unused_objects.append(self.__api_connector.get_range(object["uid"]))
            elif object["type"] == "group":
                unused_objects.append(self.__api_connector.get_group(object["uid"]))

        self.__api_connector.logout()

        return unused_objects    

    # Object Manipulation
    def change_object_color(self, uid, new_color):
        if not self.__api_connector.login(self.__user,self.__password):
            return None
        
        result = None
        obj = self.__api_connector.get_object(uid)["object"]

        if obj["type"] == "host":
            self.__api_connector.update_host(obj["uid"],color=new_color)
            result = True
        elif obj["type"] == "network":
            self.__api_connector.update_network(obj["uid"],color=new_color)
            result = True
        elif obj["type"] == "address-range":
            self.__api_connector.update_range(obj["uid"],color=new_color)
            result = True
        elif obj["type"] == "group":
            self.__api_connector.update_group(obj["uid"],color=new_color)
            result = True
        else:
            result = False

        self.__api_connector.publish()
        self.__api_connector.logout()
        return result
    def change_object_name(self, uid, new_name):
        if not self.__api_connector.login(self.__user,self.__password):
            return None
    
        result = None
        obj = self.__api_connector.get_object(uid)["object"]
        
        if obj["type"] == "host":
            self.__api_connector.update_host(obj["uid"],new_name=new_name)
            result = True
        elif obj["type"] == "network":
            self.__api_connector.update_network(obj["uid"],new_name=new_name)
            result = True
        elif obj["type"] == "address-range":
            self.__api_connector.update_range(obj["uid"],new_name=new_name)
            result = True
        elif obj["type"] == "group":
            self.__api_connector.update_group(obj["uid"],new_name=new_name)
            result = True
        else:
            result = False

        self.__api_connector.publish()
        self.__api_connector.logout()
        return result
    def delete_object(self,uid):
        if not self.__api_connector.login(self.__user,self.__password):
            return None
    
        result = None
        obj = self.__api_connector.get_object(uid)["object"]
        
        if obj["type"] == "host":
            self.__api_connector.delete_host(uid)
            result = True
        elif obj["type"] == "network":
            self.__api_connector.delete_network(uid)
            result = True
        elif obj["type"] == "address-range":
            self.__api_connector.delete_range(uid)
            result = True
        elif obj["type"] == "group":
            self.__api_connector.delete_group(uid)
            result = True
        else:
            result = False

        self.__api_connector.publish()
        self.__api_connector.logout()
        return result    
      
    # Misc
    def push_sample_objects(self):
        if not self.__api_connector.login(self.__user,self.__password):
            return None

        self.__api_connector.add_host("ACS_server","10.66.48.70")
        self.__api_connector.add_host("ACS_server2","10.66.48.71")
        self.__api_connector.add_host("Gho_h1","10.254.130.5")
        self.__api_connector.add_host("Gho_h2","10.254.130.76")
        self.__api_connector.add_host("CP_perimeter","10.66.51.136")
        self.__api_connector.add_network("mgmt_net","10.66.51.0","25")
        self.__api_connector.add_network("mgmt_net2","10.66.51.128","25")
        self.__api_connector.add_range("checkpoint_mgmt_interfaces","10.66.60.30","10.66.60.34")
        self.__api_connector.add_group("AAA_servers",["ACS_server","ACS_server2"])
        self.__api_connector.add_group("Mgmt_Networks",["mgmt_net","mgmt_net2"])
        self.__api_connector.add_group("Checkpoint",["CP_perimeter","checkpoint_mgmt_interfaces"])
        
        self.__api_connector.publish()
        self.__api_connector.logout()
