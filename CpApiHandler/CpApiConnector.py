import requests
import json
  
# This class provides direct access to the checkpoint API
# It always returns the raw JSON result from the api response
class CpApiConnector:
    def __init__(self, endpoint):
        self.__endpoint = endpoint

    # Session __endpoints
    def login(self, user, password):
        # Setting the POST data
        data = {"user":user,"password":password}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/login"
        headers = {'Content-type': 'application/json'}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            self.sid = response.json()['sid']
            self.isLoggedIn = True
            return True
        else:
            print(response.text)
            return False
    def logout(self):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/logout"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            self.sid = None
            self.isLoggedIn = False
            return True
        else:
            print(response.text)
            return False        
    def publish(self):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/publish"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False

    # Host Enpoints
    def get_host(self, uid):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"uid" : uid}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/show-host"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.text)
            return None
    def get_all_hosts(self):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"details-level":"full"}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/show-hosts"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.text)
            return None        
    def add_host(self, name, ipv4_address, ipv6_address=None):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name" : name, "ipv4-address" : ipv4_address}
        if ipv6_address!=None:
            data["ipv6-address"]=ipv6_address
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/add-host"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def update_host(self, uid, address=None, new_name=None, color=None):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"uid" : uid}
        if address!=None:
            data["ip-address"]=address
        if color!=None:
            data["color"]=color
        if new_name!=None:
            data["new-name"]=new_name
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/set-host"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def delete_host(self,uid):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"uid" : uid}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/delete-host"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False

    # Network Enpoints
    def get_network(self,uid):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"uid" : uid}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/show-network"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.text)
            return None
    def get_all_networks(self):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"details-level":"full"}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/show-networks"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.text)
            return None        
    def add_network(self, name,subnet,mask_length):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name":name, "subnet":subnet, "mask-length":mask_length}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/add-network"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def update_network(self,uid,subnet=None,mask_length=None,new_name=None,color=None):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"uid" : uid}
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
        api___endpoint = self.__endpoint + "/set-network"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def delete_network(self,uid):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"uid" : uid}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/delete-network"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    
    # Range __endpoints
    def get_range(self,uid):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"uid" : uid}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/show-address-range"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.text)
            return None
    def get_all_ranges(self):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"details-level":"full"}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/show-address-ranges"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.text)
            return None        
    def add_range(self,name,address_first,address_last):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name":name, "ip-address-first":address_first, "ip-address-last":address_last}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/add-address-range"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def update_range(self,uid,address_first=None,address_last=None,new_name=None,color=None):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"uid" : uid}
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
        api___endpoint = self.__endpoint + "/set-address-range"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def delete_range(self,uid):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"uid" : uid}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/delete-address-range"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    
    # Group __endpoints
    def get_group(self,uid):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"uid" : uid}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/show-group"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.text)
            return None
    def get_all_groups(self):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"details-level":"full"}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/show-groups"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.text)
            return None        
    def add_group(self,name,members=None):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name":name}
        if members!=None:
            data["members"]=members
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/add-group"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def update_group(self,uid,members=None,new_name=None,color=None):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"uid" : uid}
        if members!=None:
            data["members"]=members
        if color!=None:
            data["color"]=color
        if new_name!=None:
            data["new-name"]=new_name
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/set-group"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def delete_group(self,uid):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"uid" : uid}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/delete-group"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False

    # Misc
    def get_object(self,uid):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"uid" : uid}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/show-object"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.text)
            return None
    def get_unused_objects(self):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {}
        #
        # Create & Send the request
        api___endpoint = self.__endpoint + "/show-unused-objects"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api___endpoint, json=data, verify=False, headers=headers)
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