import requests
import json
from CpApiConnector import *
# defining the api-endpoint  

class CpApiHandler:
    def __init__(self, server_ip, user, password):
        self.api_connecter = CpApiConnector("https://"+server_ip+"/web_api")
        self.user = user
        self.password = password

    def get_net_objects(self):
        if not self.api_connecter.login(self.user,self.password):
            return None
     
        objects = dict()
        objects["hosts"] = list()
        objects["networks"] = list()
        objects["ranges"] = list()
        objects["groups"] = list()
        for host in self.api_connecter.get_all_hosts()["objects"]:
            objects["hosts"].append(self.api_connecter.get_host(host["name"]))
        for network in self.api_connecter.get_all_networks()["objects"]:
            objects["networks"].append(self.api_connecter.get_network(network["name"]))
        for range in self.api_connecter.get_all_ranges()["objects"]:
            objects["ranges"].append(self.api_connecter.get_range(range["name"]))
        for group in self.api_connecter.get_all_groups()["objects"]:
            objects["groups"].append(self.api_connecter.get_group(group["name"]))

        if self.api_connecter.logout():
            print("Logged Out")

        return objects