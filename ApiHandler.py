import requests
import json
import re
# defining the api-endpoint  

class ApiHandler:
    def __init__(self,endpoint):
        self.endpoint = endpoint

    def login(self,user,password):
        login_endpoint = self.endpoint + "/login"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        # Setting the POST data
        data = {"user":user,"password":password}
        #send request
        response = requests.post(url = login_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            self.sid = re.search('\"(.+)\"',response.text.split("\n")[1]).group(1)
            self.isLogged = True
            return True
        else:
            print(response.text)
            return False

    def publish(self):
        if not self.isLogged:
            return False
        login_endpoint = self.endpoint + "/publish"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'X-chkp-sid': self.sid}
        # Setting the POST data
        data = {}
        #send request
        response = requests.post(url = login_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False

    def logout(self):
        if not self.isLogged:
            return False
        login_endpoint = self.endpoint + "/logout"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'X-chkp-sid': self.sid}
        # Setting the POST data
        data = {}
        #send request
        response = requests.post(url = login_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            self.sid = None
            self.isLogged = False
            return True
        else:
            print(response.text)
            return False

    def add_host(self,name,address):
        if not self.isLogged:
            return False
        login_endpoint = self.endpoint + "/add-host"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'X-chkp-sid': self.sid}
        # Setting the POST data
        data = {"name" : name, "ip-address" : address}
        #send request
        response = requests.post(url = login_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    def set_host(self,name,address=None,color=None):
        if not self.isLogged:
            return False
        login_endpoint = self.endpoint + "/set-host"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'X-chkp-sid': self.sid}
        # Setting the POST data
        data = {"name" : name}
        if not address==None:
            data["ip-address"]=address
        if not color==None:
            data["color"]=color
        #send request
        response = requests.post(url = login_endpoint, json=data, verify=False, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(response.text)
            return False
    #not implemented
    def get_host(self,name):

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

