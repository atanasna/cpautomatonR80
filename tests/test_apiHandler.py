from CpApiHandler.CpApiHandler import *
from pprint import pprint

config = None
with open('config/config.json') as f:
    config = json.load(f)
server_ip = config["api_credentials"]["address"]
user = config["api_credentials"]["username"]
password = config["api_credentials"]["password"]

api_handler = CpApiHandler(server_ip,user,password)
api_handler.push_sample_objects()

# Test Session Endpoints
def test_get_net_objects():
    objects = api_handler.get_net_objects()
    pprint(objects)
    assert len(objects["hosts"])>0 and len(objects["networks"])>0 and len(objects["ranges"])>0 and len(objects["groups"])>0

def test_get_unused_net_objects():
    objects = api_handler.get_unused_net_objects()
    pprint(objects)
    assert len(objects) > 0