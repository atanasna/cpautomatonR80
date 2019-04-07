import requests
import json
import time
from pprint import pprint
from threading import Thread
from CpApiConnector import *
# defining the api-endpoint  

class CpApiHandler:
    def __init__(self, server_ip, user, password):
        self.__api_connector = CpApiConnector("https://"+server_ip+"/web_api")
        self.__user = user
        self.__password = password
        self.__isLoggedIn = False
        self.__apiSid = None
        self.login()

    def __del__(self):
        self.logout()

    def login(self):
        self.__apiSid = self.__api_connector.login(self.__user,self.__password)["sid"]
        self.__isLoggedIn = True
        self.keepalive_thread = Thread(target=self.keepalive)
        self.keepalive_thread.start()
    def logout(self):
        self.__api_connector.discard(self.__apiSid)
        self.__api_connector.logout(self.__apiSid)
        self.__isLoggedIn = False
        self.keepalive_thread.join()
    def keepalive(self):
        while self.__isLoggedIn:
            print self.__isLoggedIn
            time.sleep(5)
            self.__api_connector.keepalive(self.__apiSid)

    # Object Getters
    def get_net_objects(self):
        
        objects = dict()
        objects["hosts"] = list()
        objects["networks"] = list()
        objects["ranges"] = list()
        objects["groups"] = list()
        for host in self.__api_connector.get_all_hosts(self.__apiSid)["objects"]:
            objects["hosts"].append(self.__api_connector.get_host(self.__apiSid, host["uid"]))
        for network in self.__api_connector.get_all_networks(self.__apiSid)["objects"]:
            objects["networks"].append(self.__api_connector.get_network(self.__apiSid, network["uid"]))
        for range in self.__api_connector.get_all_ranges(self.__apiSid)["objects"]:
            objects["ranges"].append(self.__api_connector.get_range(self.__apiSid, range["uid"]))
        for group in self.__api_connector.get_all_groups(self.__apiSid)["objects"]:
            objects["groups"].append(self.__api_connector.get_group(self.__apiSid, group["uid"]))

        return objects
    def get_unused_net_objects(self):
        unused_objects = list()

        for object in self.__api_connector.get_unused_objects(self.__apiSid)["objects"]:
            if object["type"] == "host":
                unused_objects.append(self.__api_connector.get_host(self.__apiSid,object["uid"]))
            elif object["type"] == "network":
                unused_objects.append(self.__api_connector.get_network(self.__apiSid,object["uid"]))
            elif object["type"] == "address-range":
                unused_objects.append(self.__api_connector.get_range(self.__apiSid,object["uid"]))
            elif object["type"] == "group":
                unused_objects.append(self.__api_connector.get_group(self.__apiSid,object["uid"]))

        return unused_objects    

    # Object Manipulation
    def change_object_color(self, uid, new_color):   
        result = None
        obj = self.__api_connector.get_object(self.__apiSid, uid)["object"]

        if obj["type"] == "host":
            self.__api_connector.update_host(self.__apiSid, obj["uid"], color=new_color)
            result = True
        elif obj["type"] == "network":
            self.__api_connector.update_network(self.__apiSid, obj["uid"], color=new_color)
            result = True
        elif obj["type"] == "address-range":
            self.__api_connector.update_range(self.__apiSid, obj["uid"], color=new_color)
            result = True
        elif obj["type"] == "group":
            self.__api_connector.update_group(self.__apiSid, obj["uid"], color=new_color)
            result = True
        else:
            result = False
        self.__api_connector.publish(self.__apiSid)

        return result
    def change_object_name(self, uid, new_name):
        result = None
        obj = self.__api_connector.get_object(self.__apiSid, uid)["object"]
        
        if obj["type"] == "host":
            self.__api_connector.update_host(self.__apiSid, obj["uid"],new_name=new_name)
            result = True
        elif obj["type"] == "network":
            self.__api_connector.update_network(self.__apiSid, obj["uid"],new_name=new_name)
            result = True
        elif obj["type"] == "address-range":
            self.__api_connector.update_range(self.__apiSid, obj["uid"],new_name=new_name)
            result = True
        elif obj["type"] == "group":
            self.__api_connector.update_group(self.__apiSid, obj["uid"],new_name=new_name)
            result = True
        else:
            result = False

        self.__api_connector.publish(self.__apiSid)

        return result
    def delete_object(self,uid):
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

        self.__api_connector.publish(self.__apiSid)
        return result    

    # Misc
    def push_sample_objects(self):
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
        
        self.__api_connector.publish(self.__apiSid)
    def test_api_endpoint(self):
        #where_used = self.__api_connector.get_where_used(uid)
        #rules = where_used['used-directly']['access-control-rules']
        #nat_rules = where_used['used-directly']['nat-rules']
        #objs = where_used['used-directly']['objects']
        #pprint("-------------")
        #for rule in rules:
        #    pprint("=============")
        #    pprint("Layer Name: " + rule["layer"]["name"])
        #    pprint("Layer ID: " + rule["layer"]["uid"])
        #    pprint("Layer Name: " + rule["rule"]["name"])
        #    pprint("Layer Name: " + rule["rule"]["uid"])
        #pprint("-------------")
        #pprint(nat_rules)
        #pprint("-------------")
        #pprint(objs)
        #pprint("-------------")

        #pprint(self.__api_connector.get_access_rule('ae49bb4d-0c75-4eb5-842b-8fac3ceae3ec','bf7d4c27-5116-40db-98f8-0d4118089879'))
        #self.__api_connector.delete_access_rule('4f4db11b-5f97-453c-8d5b-a1261e009ee9','0d7b286b-b6b4-40e3-92a1-e010dc38bdb7')
        pprint("0")
        #self.__api_connector.update_access_rule('ae49bb4d-0c75-4eb5-842b-8fac3ceae3ec','bf7d4c27-5116-40db-98f8-0d4118089879',enabled=False)
        self.__api_connector.add_access_rule('ae49bb4d-0c75-4eb5-842b-8fac3ceae3ec', position=4, name="Bobsana2", sources=['c9489189-e4d4-44f9-af21-f0cf137ae679','213506ff-a375-a54b-8533-8eb8edd5e87d'], destinations=['095915f6-4499-4ce2-8eda-c5af6eab0b1c','dd944cca-5d65-49e8-abb3-211438bbe521'], comments="babati e koza")
        pprint("1")