from ObjectsHandler.CpGroup import *
from ObjectsHandler.CpHost import *
from ObjectsHandler.CpNetwork import *
from ObjectsHandler.CpRange import *
from ApiHandler import *
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)



#if mgmt.add_host("h_2","10.10.10.11"):
#    print("Host added")

#if mgmt.set_host("h_2",color="brown",new_name="petko"):
#    print("Changed to Green h_2")

#print(mgmt.get_all_groups())
#print (mgmt.get_group("babinite_checkpointcheta"))
#if mgmt.delete_group("babinite_checkpointcheta"):
#    print("Deleted")
#if mgmt.add_range("cp_per_range2","10.10.10.34","10.10.10.60"):
#    print("Added")
#if mgmt.set_range("cp_per_range",address_first="10.20.30.34", address_last="10.20.30.124",color="green",new_name="cp_per_range12"):
#    print("Changed Network")
#mgmt.add_host("node1","10.10.44.5")
#mgmt.add_host("node2","10.10.44.6")
#mgmt.add_host("node3","10.10.44.7")
def get_net_objects(api):
    if not api.login("king","passport"):
        return None
 
    objects = dict()
    objects["hosts"] = list()
    objects["networks"] = list()
    objects["ranges"] = list()
    objects["groups"] = list()
    for host in api.get_all_hosts()["objects"]:
        objects["hosts"].append(api.get_host(host["name"]))
    for network in api.get_all_networks()["objects"]:
        objects["networks"].append(api.get_network(network["name"]))
    for range in api.get_all_ranges()["objects"]:
        objects["ranges"].append(api.get_range(range["name"]))
    for group in api.get_all_groups()["objects"]:
        objects["groups"].append(api.get_group(group["name"]))

    if api.logout():
        print("Logged Out")

    return objects

api = ApiHandler("https://34.241.216.138/web_api")
objects = get_net_objects(api)
pp.pprint(objects)
#for host in hosts["objects"]:
#    host_obj = CpHost(host["name"],host["ipv4-address"])
#    print "-----"
#    print host_obj.name
#    print host_obj.address
##if mgmt.publish():
##    print("Published")
