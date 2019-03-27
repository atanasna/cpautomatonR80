import requests
import json
# defining the api-endpoint  

class CpApiConnector:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    # Session Endpoints
    def login(self, user, password):
        # Setting the POST data
        data = {"user":user,"password":password}
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/login"
        headers = {'Content-type': 'application/json'}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
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
        api_endpoint = self.endpoint + "/logout"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
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
        api_endpoint = self.endpoint + "/publish"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False

    # Host Enpoints
    def get_host(self, name):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name" : name}
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/show-host"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
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
        data = {}
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/show-hosts"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
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
        api_endpoint = self.endpoint + "/add-host"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def set_host(self, name, address=None, new_name=None, color=None):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name" : name}
        if address!=None:
            data["ip-address"]=address
        if color!=None:
            data["color"]=color
        if new_name!=None:
            data["new-name"]=new_name
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/set-host"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def delete_host(self,name):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name" : name}
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/delete-host"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False

    # Network Enpoints
    def get_network(self,name):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name" : name}
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/show-network"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
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
        data = {}
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/show-networks"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.text)
            return None        
    def add_network(self,name,subnet,mask_length):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name":name, "subnet":subnet, "mask-length":mask_length}
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/add-network"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def set_network(self,name,subnet=None,mask_length=None,new_name=None,color=None):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name" : name}
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
        api_endpoint = self.endpoint + "/set-network"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def delete_network(self,name):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name" : name}
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/delete-network"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    
    # Range Endpoints
    def get_range(self,name):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name" : name}
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/show-address-range"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
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
        data = {}
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/show-address-ranges"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
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
        api_endpoint = self.endpoint + "/add-address-range"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def set_range(self,name,address_first=None,address_last=None,new_name=None,color=None):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name" : name}
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
        api_endpoint = self.endpoint + "/set-address-range"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def delete_range(self,name):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name" : name}
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/delete-address-range"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    
    # Group Endpoints
    def get_group(self,name):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name" : name}
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/show-group"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
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
        data = {}
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/show-groups"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
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
        api_endpoint = self.endpoint + "/add-group"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def set_group(self,name,members=None,new_name=None,color=None):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name" : name}
        if members!=None:
            data["members"]=members
        if color!=None:
            data["color"]=color
        if new_name!=None:
            data["new-name"]=new_name
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/set-group"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def delete_group(self,name):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name" : name}
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/delete-group"
        headers = {'Content-type': 'application/json', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False