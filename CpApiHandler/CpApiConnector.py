import requests
import json
from pprint import pprint

  
# This class provides direct access to the checkpoint API
# It always returns the raw JSON result from the api response
class CpApiConnector:
    def __init__(self, endpoint):
        self.__endpoint = endpoint

    # Session Endpoints ------------------------------------------
    def login(self, user, password):
        # Setting the POST data
        data = {"user":user,"password":password}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/login"
        return self.__send_request(api_endpoint, data)
    def logout(self, sid):
        # Setting the POST data
        data = {}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/logout"
        return self.__send_request(api_endpoint, data, sid)  
    def discard(self,sid):
        # Setting the POST data
        data = {}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/discard"
        return self.__send_request(api_endpoint, data, sid)
    def keepalive(self, sid):
        # Setting the POST data
        data = {}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/keepalive"
        return self.__send_request(api_endpoint, data, sid)     
    def publish(self, sid):
        # Setting the POST data
        data = {}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/publish"
        return self.__send_request(api_endpoint, data, sid)

    # Objects Endpoints ------------------------------------------
    # Host Enpoints
    def get_host(self, sid, host_uid):
        # Setting the POST data
        data = {"uid" : host_uid}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/show-host"
        return self.__send_request(api_endpoint, data, sid)
    def get_all_hosts(self, sid):
        # Setting the POST data
        data = {"details-level":"full"}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/show-hosts"
        return self.__send_request(api_endpoint, data, sid)      
    def add_host(self, sid, name, ipv4_address, ipv6_address=None):
        # Setting the POST data
        data = {"name" : name, "ipv4-address" : ipv4_address}
        if ipv6_address!=None:
            data["ipv6-address"]=ipv6_address
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/add-host"
        return self.__send_request(api_endpoint, data, sid)
    def update_host(self, sid, host_uid, address=None, new_name=None, color=None):
        # Setting the POST data
        data = {"uid" : host_uid}
        if address!=None:
            data["ip-address"]=address
        if color!=None:
            data["color"]=color
        if new_name!=None:
            data["new-name"]=new_name
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/set-host"
        return self.__send_request(api_endpoint, data, sid)
    def delete_host(self, sid, host_uid):
        # Setting the POST data
        data = {"uid" : host_uid}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/delete-host"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': sid}
        return self.__send_request(api_endpoint, data, sid)

    # Network Enpoints
    def get_network(self, sid, network_uid):
        # Setting the POST data
        data = {"uid" : network_uid}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/show-network"
        return self.__send_request(api_endpoint, data, sid)
    def get_all_networks(self, sid):
        # Setting the POST data
        data = {"details-level":"full"}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/show-networks"
        return self.__send_request(api_endpoint, data, sid)     
    def add_network(self, sid, name, subnet, mask_length):
        # Setting the POST data
        data = {"name":name, "subnet":subnet, "mask-length":mask_length}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/add-network"
        return self.__send_request(api_endpoint, data, sid)
    def update_network(self, sid, network_uid, subnet=None,mask_length=None,new_name=None,color=None):
        # Setting the POST data
        data = {"uid" : network_uid}
        if subnet!=None:
            data["subnet"]=subnet
        if mask_length!=None:
            data["mask-length"]=mask_length
        if color!=None:
            data["color"]=color
        if new_name!=None:
            data["new-name"]=new_name
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/set-network"
        return self.__send_request(api_endpoint, data, sid)
    def delete_network(self, sid, network_uid):
        # Setting the POST data
        data = {"uid" : network_uid}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/delete-network"
        return self.__send_request(api_endpoint, data, sid)
    
    # Range Endpoints
    def get_range(self, sid, range_uid):
        # Setting the POST data
        data = {"uid" : range_uid}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/show-address-range"
        return self.__send_request(api_endpoint, data, sid)
    def get_all_ranges(self, sid):
        # Setting the POST data
        data = {"details-level":"full"}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/show-address-ranges"
        return self.__send_request(api_endpoint, data, sid)     
    def add_range(self, sid, name,address_first,address_last):
        # Setting the POST data
        data = {"name":name, "ip-address-first":address_first, "ip-address-last":address_last}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/add-address-range"
        return self.__send_request(api_endpoint, data, sid)
    def update_range(self, sid, range_uid, address_first=None,address_last=None,new_name=None,color=None):
        # Setting the POST data
        data = {"uid" : range_uid}
        if address_first!=None:
            data["ip-address-first"]=address_first
        if address_last!=None:
            data["ip-address-last"]=address_last
        if color!=None:
            data["color"]=color
        if new_name!=None:
            data["new-name"]=new_name
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/set-address-range"
        return self.__send_request(api_endpoint, data, sid)
    def delete_range(self, sid, range_uid):
        # Setting the POST data
        data = {"uid" : range_uid}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/delete-address-range"
        return self.__send_request(api_endpoint, data, sid)
    
    # Group Endpoints
    def get_group(self, sid, group_uid):
        # Setting the POST data
        data = {"uid" : group_uid}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/show-group"
        return self.__send_request(api_endpoint, data, sid)
    def get_all_groups(self, sid):
        # Setting the POST data
        data = {"details-level":"full"}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/show-groups"
        return self.__send_request(api_endpoint, data, sid)      
    def add_group(self, sid, name, members=None):
        # Setting the POST data
        data = {"name":name}
        if members!=None:
            data["members"]=members
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/add-group"
        return self.__send_request(api_endpoint, data, sid)
    def update_group(self, sid, group_uid, members=None,new_name=None,color=None):
        # Setting the POST data
        data = {"uid" : group_uid}
        if members!=None:
            data["members"]=members
        if color!=None:
            data["color"]=color
        if new_name!=None:
            data["new-name"]=new_name
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/set-group"
        return self.__send_request(api_endpoint, data, sid)
    def delete_group(self, sid, group_uid):
        # Setting the POST data
        data = {"uid" : group_uid}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/delete-group"
        return self.__send_request(api_endpoint, data, sid)

    # Policy Endpoints ------------------------------------------
    # AccessLayers Enpoints
    def get_access_layer(self, sid, layer_uid):
        # Setting the POST data
        data = {"uid" : layer_uid }
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/show-access-layer"
        return self.__send_request(api_endpoint, data, sid)
    def add_access_layer(self, sid, name, firewall=True, url_filtering=False, content_awareness=False, mobile=False, shared=False):
        # Setting the POST data
        data = dict()
        data["name"] = name
        data["firewall"] = firewall
        data["applications-and-url-filtering"] = url_filtering
        data["content-awareness"] = content_awareness
        data["mobile-access"] = mobile
        data["shared"] = shared
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/add-access-layer"
        return self.__send_request(api_endpoint, data, sid)
    def update_access_layer(self, sid, layer_uid, new_name=None, firewall=None, url_filtering=None, content_awareness=None, mobile=None, shared=None):
        # Setting the POST data
        data = {"uid" : layer_uid} 
        if new_name!=None:
            data["new-name"] = new_name
        if firewall==True or firewall==False:
            data["firewall"] = firewall
        if url_filtering==True or url_filtering==False:
            data["applications-and-url-filtering"] = url_filtering
        if content_awareness==True or content_awareness==False:
            data["content-awareness"] = content_awareness
        if mobile==True or mobile==False:
            data["mobile-access"] = mobile
        if shared==True or shared==False:
            data["shared"] = shared
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/set-access-layer"
        return self.__send_request(api_endpoint, data, sid)
    def delete_access_layer(self, sid, layer_uid):
        # Setting the POST data
        data = {"uid" : layer_uid}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/delete-access-layer"
        return self.__send_request(api_endpoint, data, sid)
    
    # AccessRules Endpoins
    def get_access_rule(self, sid, layer_uid, rule_uid):
        # Setting the POST data
        data = {"uid" : rule_uid, "layer" : layer_uid}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/show-access-rule"
        return self.__send_request(api_endpoint, data, sid)
    def add_access_rule(self, sid, layer_uid, position="top", name=None, action="Accept", enabled=True, sources=list(), destinations=list(), services=list(), comments=None):
        # Setting the POST data
        data = dict()
        data["layer"] = layer_uid
        data["position"] = position
        data["enabled"] = enabled
        data["name"] = name
        data["source"] = sources
        data["destination"] = destinations
        data["service"] = services
        data["action"] = action
        data["comments"] = comments
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/add-access-rule"
        return self.__send_request(api_endpoint, data, sid)
    def update_access_rule(self, sid, layer_uid, rule_uid, action=None, new_name=None, enabled=None, add_srcs=list(), rem_srcs=list(), add_dsts=list(), rem_dsts=list(), add_services=list(), rem_services=list(),comments=None):
        if add_srcs and rem_srcs or add_dsts and rem_dsts or add_services and rem_services:
            pprint("You can't use REM and ADD at the same time")
            return False
        #
        # Setting the POST data
        data = {"uid" : rule_uid, "layer" : layer_uid}
        if action!=None:
            data["action"] = action
        if new_name!=None:
            data["new-name"] = new_name
        if enabled==True or enabled==False:
            data["enabled"] = enabled

        if add_srcs or rem_srcs:
            data["source"] = dict()
            if add_srcs:
                data["source"]["add"] = add_srcs
            if rem_srcs:
                data["source"]["remove"] = rem_srcs
        if add_dsts or rem_dsts:
            data["destination"] = dict()
            if add_dsts:
                data["destination"]["add"] = add_dsts
            if rem_dsts:
                data["destination"]["remove"] = rem_dsts
        if add_services or rem_services:
            data["service"] = dict()
            if add_services:
                data["service"]["add"] = add_services
            if rem_services:
                data["service"]["remove"] = rem_services
        if comments:
            data["comments"] = comments
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/set-access-rule"
        return self.__send_request(api_endpoint, data, sid)
    def delete_access_rule(self, sid, layer_uid, rule_uid):
        # Setting the POST data
        data = {"uid" : rule_uid, "layer" : layer_uid}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/delete-access-rule"
        return self.__send_request(api_endpoint, data, sid)

    # NatRules Endpoints
    def get_nat_rule(self, sid, package, nat_rule_uid):
        # Setting the POST data
        data = {"uid" : nat_rule_uid, "package" : package}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/show-nat-rule"
        return self.__send_request(api_endpoint, data, sid)
    def add_nat_rule(self, sid, package, position="bottom", enabled=False, o_src="Any", o_dst="Any", o_service="Any", t_src="Original", t_dst="Original", t_service="Original",comment=""):
        # Setting the POST data
        data = dict()
        data["package"] = package
        data["position"] = position
        data["enabled"] = enabled
        data["original-source"] = o_src
        data["original-destination"] = o_dst
        data["original-service"] = o_service
        data["translated-source"] = t_src
        data["translated-destination"] = t_dst
        data["translated-service"] = t_service
        data["comments"] = comment
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/add-nat-rule"
        return self.__send_request(api_endpoint, data, sid)
    #not working
    def update_nat_rule(self, sid, package, nat_rule_uid, position=None, enabled=None, o_src=None, o_dst=None, o_service=None, t_src=None, t_dst=None, t_service=None,comment=None):
        # Setting the POST data
        data = {"uid" : nat_rule_uid, "package" : package}
        if position:
            data["position"] = position
        if enabled==True or enabled==False:
            data["enabled"] = enabled
        if o_src:
            data["original-source"] = o_src
        if o_dst:
            data["original-destination"] = o_dst
        if o_service:
            data["original-service"] = o_service
        if t_src:
            data["translated-source"] = t_src
        if t_dst:
            data["translated-destination"] = t_dst
        if t_service:
            data["translated-service"] = t_service
        if comment:
            data["comments"] = comment
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/set-nat-rule"
        return self.__send_request(api_endpoint, data, sid)
    def delete_nat_rule(self, sid, package, nat_rule_uid):
        # Setting the POST data
        data = {"uid" : nat_rule_uid, "package" : package}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/delete-nat-rule"
        return self.__send_request(api_endpoint, data, sid)
    
    # Misc ------------------------------------------
    def get_object(self, sid, object_uid):
        # Setting the POST data
        data = {"uid" : object_uid}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/show-object"
        return self.__send_request(api_endpoint, data, sid)
    def get_unused_objects(self, sid):
        # Setting the POST data
        data = {}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/show-unused-objects"
        return self.__send_request(api_endpoint, data, sid)     
    def get_where_used(self,sid, object_uid):
        # Setting the POST data
        data = {"uid":object_uid}
        #
        # Create & Send the request
        api_endpoint = self.__endpoint + "/where-used"
        return self.__send_request(api_endpoint, data, sid)     
             
    def __send_request(self, endpoint, data, sid=None):
        headers = {'Content-type': 'application/json'}
        if sid != None:
            headers['X-chkp-sid'] = sid
        response = requests.post(url = endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.text)
            return None      

    # Access Rules __endpoints
    #def get_access_rule(self, uid, layer):
    #def get_all_access_rules(self):
    #def update_access_rule(self, uid, layer):
    #def detele_access_rule(serf, uid, layer):