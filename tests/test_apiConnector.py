from CpApiHandler.CpApiConnector import *
from pprint import pprint

config = None
with open('config/config.json') as f:
    config = json.load(f)
server_ip = config["api_credentials"]["address"]
user = config["api_credentials"]["username"]
password = config["api_credentials"]["password"]

api_connector = CpApiConnector("https://"+server_ip+"/web_api")

# Test Session Endpoints
def test_login():
    sid = api_connector.login(user,password)["sid"]
    api_connector.logout(sid)
    assert sid != None
def test_logout():
    sid = api_connector.login(user,password)["sid"]
    result = api_connector.logout(sid)
    assert result["message"] == "OK"
def test_discard():
    sid = api_connector.login(user,password)["sid"]
    result = api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["message"] == "OK"
def test_keepalive():
    sid = api_connector.login(user,password)["sid"]
    result = api_connector.keepalive(sid)
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["message"] == "OK"
def test_publish():
    sid = api_connector.login(user,password)["sid"]
    result = api_connector.publish(sid)
    api_connector.logout(sid)
    assert result["task-id"] != None

# Test Host Endpoints
def test_add_host():
    sid = api_connector.login(user,password)["sid"]
    result = api_connector.add_host(sid,"host1","10.10.10.50")
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["uid"] != None
def test_delete_host():
    sid = api_connector.login(user,password)["sid"]
    host = api_connector.add_host(sid,"host2","10.10.10.50")
    result = api_connector.delete_host(sid,host["uid"])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["message"] == "OK"
def test_update_host():
    sid = api_connector.login(user,password)["sid"]
    host = api_connector.add_host(sid,"host3","10.10.10.50")
    result = api_connector.update_host(sid,host["uid"],new_name="new_host",address="10.11.12.13",color="yellow")
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["name"] == "new_host" and result["ipv4-address"] == "10.11.12.13"
def test_get_host():
    sid = api_connector.login(user,password)["sid"]
    host = api_connector.add_host(sid,"host4","10.10.10.50")
    result = api_connector.get_host(sid,host["uid"])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["uid"] != None
def test_get_all_hosts():
    sid = api_connector.login(user,password)["sid"]
    hosts = api_connector.get_all_hosts(sid)
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert len(hosts)>0

# Test Network Endpoints
def test_add_network():
    sid = api_connector.login(user,password)["sid"]
    result = api_connector.add_network(sid,"net1","10.10.10.0","24")
    
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["uid"] != None
def test_delete_network():
    sid = api_connector.login(user,password)["sid"]
    network = api_connector.add_network(sid,"net2","10.10.10.0","24")
    result = api_connector.delete_network(sid,network["uid"])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["message"] == "OK"
def test_update_network():
    sid = api_connector.login(user,password)["sid"]
    network = api_connector.add_network(sid,"net3","10.10.10.0","24")
    result = api_connector.update_network(sid,network["uid"],new_name="new_net",subnet="10.11.12.0",mask_length="25", color="yellow")
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["name"] == "new_net" and result["subnet4"] == "10.11.12.0" and result["mask-length4"] == 25
def test_get_network():
    sid = api_connector.login(user,password)["sid"]
    network = api_connector.add_network(sid,"net4","10.10.10.0","24")
    result = api_connector.get_network(sid,network["uid"])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["uid"] != None
def test_get_all_networks():
    sid = api_connector.login(user,password)["sid"]
    networks = api_connector.get_all_networks(sid)
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert len(networks)>0

# Test Range Endpoints
def test_add_range():
    sid = api_connector.login(user,password)["sid"]
    result = api_connector.add_range(sid,"range1","10.10.10.0","10.10.10.20")
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["uid"] != None
def test_delete_range():
    sid = api_connector.login(user,password)["sid"]
    range = api_connector.add_range(sid,"range2","10.10.10.0","10.10.10.20")
    result = api_connector.delete_range(sid,range["uid"])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["message"] == "OK"
def test_update_range():
    sid = api_connector.login(user,password)["sid"]
    range = api_connector.add_range(sid,"range3","10.10.10.0","10.10.10.20")
    result = api_connector.update_range(sid,range["uid"],new_name="range_new",address_first="10.11.12.0",address_last="10.11.12.25", color="yellow")
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["name"] == "range_new" and result["ipv4-address-first"] == "10.11.12.0" and result["ipv4-address-last"] == "10.11.12.25"
def test_get_range():
    sid = api_connector.login(user,password)["sid"]
    range = api_connector.add_range(sid,"range4","10.10.10.0","10.10.10.60")
    result = api_connector.get_range(sid,range["uid"])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["uid"] != None
def test_get_all_range():
    sid = api_connector.login(user,password)["sid"]
    ranges = api_connector.get_all_ranges(sid)
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert len(ranges)>0

# Test Group Endpoints
def test_add_group():
    sid = api_connector.login(user,password)["sid"]
    result = api_connector.add_group(sid,"group1",members=[])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["uid"] != None
def test_delete_group():
    sid = api_connector.login(user,password)["sid"]
    group = api_connector.add_group(sid,"group2", members=[])
    result = api_connector.delete_group(sid, group["uid"])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["message"] == "OK"
def test_update_group():
    sid = api_connector.login(user,password)["sid"]
    range1 = api_connector.add_range(sid,"in_group_range1","10.10.10.0","10.10.10.20")
    range2 = api_connector.add_range(sid,"in_group_range2","10.10.10.44","10.10.10.100")
    group = api_connector.add_group(sid,"group3", members=[])
    result = api_connector.update_group(sid,group["uid"],new_name="group_new",members=[range1["uid"],range2["uid"]], color="yellow")
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["name"] == "group_new" and len(result["members"]) > 0 
def test_get_group():
    sid = api_connector.login(user,password)["sid"]
    group = api_connector.add_group(sid,"group4", members=[])
    result = api_connector.get_group(sid,group["uid"])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["uid"] != None
def test_get_all_groups():
    sid = api_connector.login(user,password)["sid"]
    groups = api_connector.get_all_groups(sid)
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert len(groups)>0

# Test Access-Layer Endpoints
def test_add_access_layer():
    sid = api_connector.login(user,password)["sid"]
    result = api_connector.add_access_layer(sid,"test_layer")
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["uid"] != None
def test_delete_access_layer():
    sid = api_connector.login(user,password)["sid"]
    layer = api_connector.add_access_layer(sid,"test_layer")
    result = api_connector.delete_access_layer(sid, layer["uid"])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["message"] == "OK"
def test_update_access_layer():
    sid = api_connector.login(user,password)["sid"]
    layer = api_connector.add_access_layer(sid,"test_layer")
    result = api_connector.update_access_layer(sid,layer["uid"],mobile=True,shared=True)
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["mobile-access"] == True and result["shared"] == True
def test_get_access_layer():
    sid = api_connector.login(user,password)["sid"]
    layer = api_connector.add_access_layer(sid,"test_layer")
    result = api_connector.get_access_layer(sid,layer["uid"])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["uid"] != None

# Test Access-Rule Endpoints
def test_add_access_rule():
    sid = api_connector.login(user,password)["sid"]
    layer = api_connector.add_access_layer(sid,"test_layer")
    host1 = api_connector.add_host(sid,"host1","10.10.10.50")
    host2 = api_connector.add_host(sid,"host2","12.12.12.50")
    result = api_connector.add_access_rule(sid,"test_layer", sources=[host1["uid"],host2["uid"]], destinations=[host1["uid"],host2["uid"]])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["uid"] != None
def test_delete_access_rule():
    sid = api_connector.login(user,password)["sid"]
    layer = api_connector.add_access_layer(sid,"test_layer")
    host1 = api_connector.add_host(sid,"host1","10.10.10.50")
    host2 = api_connector.add_host(sid,"host2","12.12.12.50")
    rule = api_connector.add_access_rule(sid,"test_layer", sources=[host1["uid"],host2["uid"]], destinations=[host1["uid"],host2["uid"]])
    result = api_connector.delete_access_rule(sid, layer["uid"], rule["uid"])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["message"] == "OK"
def test_update_access_rule():
    sid = api_connector.login(user,password)["sid"]
    #Prepare
    layer = api_connector.add_access_layer(sid,"test_layer")
    host1 = api_connector.add_host(sid,"host1","10.10.10.50")
    host2 = api_connector.add_host(sid,"host2","12.12.12.50")
    rule = api_connector.add_access_rule(sid,"test_layer", name="test_rule1", sources=[host1["uid"],host2["uid"]], destinations=[host1["uid"],host2["uid"]])
    
    result = api_connector.update_access_rule(sid, layer["uid"], rule["uid"], new_name="new_test_rule1", rem_srcs=[host1["uid"]], rem_dsts=[host1["uid"]])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["name"] == "new_test_rule1" and len(result["source"]) == 1 and len(result["destination"]) == 1
def test_get_access_rule():
    sid = api_connector.login(user,password)["sid"]
    layer = api_connector.add_access_layer(sid,"test_layer")
    host1 = api_connector.add_host(sid,"host1","10.10.10.50")
    host2 = api_connector.add_host(sid,"host2","12.12.12.50")
    rule = api_connector.add_access_rule(sid,"test_layer", sources=[host1["uid"],host2["uid"]], destinations=[host1["uid"],host2["uid"]])
    result = api_connector.get_access_rule(sid, layer["uid"], rule["uid"])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["uid"] != None

# Test NAT-Rule Endpoints
def test_add_nat_rule():
    sid = api_connector.login(user,password)["sid"]
    o_src = api_connector.add_host(sid,"o_src","10.10.10.10")
    o_dst= api_connector.add_host(sid,"o_dst","10.10.10.50")
    t_src = api_connector.add_host(sid,"t_src","12.12.12.10")
    t_dst = api_connector.add_host(sid,"t_dst","12.12.12.50")
    result = api_connector.add_nat_rule(sid,"Corporate_Policy", o_src=o_src["uid"],o_dst=o_dst["uid"],t_src=t_src["uid"],t_dst=t_dst["uid"])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["uid"] != None
def test_delete_nat_rule():
    sid = api_connector.login(user,password)["sid"]
    o_src = api_connector.add_host(sid,"o_src","10.10.10.10")
    o_dst= api_connector.add_host(sid,"o_dst","10.10.10.50")
    t_src = api_connector.add_host(sid,"t_src","12.12.12.10")
    t_dst = api_connector.add_host(sid,"t_dst","12.12.12.50")
    nat_rule = api_connector.add_nat_rule(sid,"Corporate_Policy", o_src=o_src["uid"],o_dst=o_dst["uid"],t_src=t_src["uid"],t_dst=t_dst["uid"])
    result = api_connector.delete_nat_rule(sid, "Corporate_Policy", nat_rule["uid"])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["message"] == "OK"
def test_update_nat_rule():
    sid = api_connector.login(user,password)["sid"]
    #Prepare
    o_src = api_connector.add_host(sid,"o_src","10.10.10.10")
    o_dst= api_connector.add_host(sid,"o_dst","10.10.10.50")
    t_src = api_connector.add_host(sid,"t_src","12.12.12.10")
    t_dst = api_connector.add_host(sid,"t_dst","12.12.12.50")
    nat_rule = api_connector.add_nat_rule(sid,"Corporate_Policy", o_src=o_src["uid"],o_dst=o_dst["uid"],t_src=t_src["uid"],t_dst=t_dst["uid"])
    
    result = api_connector.update_nat_rule(sid, "Corporate_Policy", nat_rule["uid"], enabled=True, o_src=o_dst["uid"], o_dst=o_src["uid"], t_src=t_dst["uid"], t_dst=t_src["uid"])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["enabled"] == True and result["original-source"]["name"] == "o_dst" and result["translated-destination"]["name"] == "t_src"
def test_get_nat_rule():
    sid = api_connector.login(user,password)["sid"]
    o_src = api_connector.add_host(sid,"o_src","10.10.10.10")
    o_dst= api_connector.add_host(sid,"o_dst","10.10.10.50")
    t_src = api_connector.add_host(sid,"t_src","12.12.12.10")
    t_dst = api_connector.add_host(sid,"t_dst","12.12.12.50")
    nat_rule = api_connector.add_nat_rule(sid,"Corporate_Policy", o_src=o_src["uid"],o_dst=o_dst["uid"],t_src=t_src["uid"],t_dst=t_dst["uid"])
    result = api_connector.get_nat_rule(sid, "Corporate_Policy", nat_rule["uid"])
    api_connector.discard(sid)
    api_connector.logout(sid)
    assert result["uid"] != None
# Misc
#def test_publish_then_discard():
#    sid = api_connector.login(user,password)["sid"]
#    result = api_connector.add_range(sid,"range1","10.10.10.0","10.10.10.20")
#    api_connector.publish(sid)
#    api_connector.discard(sid)
#    api_connector.logout(sid)
#    assert result["uid"] != None