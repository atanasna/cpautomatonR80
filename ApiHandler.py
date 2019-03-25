import requests
import json
import re
# defining the api-endpoint  

class ApiHandler:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def login(self, user, password):
        # Setting the POST data
        data = {"user":user,"password":password}
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/login"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            self.sid = re.search('\"(.+)\"',response.text.split("\n")[1]).group(1)
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
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'X-chkp-sid': self.sid}
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
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'X-chkp-sid': self.sid}
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
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
            return False
    def add_host(self, name, ipv4_address, ipv6_address=None):
        # Initial checks
        if not self.isLoggedIn:
            return False
        #
        # Setting the POST data
        data = {"name" : name, "ipv4-address" : address}
        if ipv6_address!=None:
            data["ipv6-address"]=ipv6_address
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/add-host"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'X-chkp-sid': self.sid}
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
            data["new-name":new_name]
        #
        # Create & Send the request
        api_endpoint = self.endpoint + "/set-host"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'X-chkp-sid': self.sid}
        response = requests.post(url = api_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False

    # Network Enpoints
    # Range Endpoints
    # Group Endpoints
    
    #not implemented
    def add_network(self,name,subnet,mask):
    def set_network(self,name,subnet=None,mask=None):
    def get_network(self,name):

    #def add_range(self,name):
    #def set_range(self,name):
    #def get_range(self,name):
    
    #def add_group(self,name):
    #def set_group(self,name):
    #def get_group(self,name):

mgmt = ApiHandler("https://3.120.151.136/web_api")
if mgmt.login("king","passport"):
    print("Logged In")
if mgmt.set_host("h_1",color="black"):
    print("Host added")
if mgmt.publish():
    print("Published")
if mgmt.logout():
    print("Logged Out")