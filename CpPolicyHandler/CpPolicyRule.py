import copy

class CpPolicyRule:
    def __init__(self, rule_uid, enabled, hits=0, rule_name=None):
        self.uid = rule_uid
        self.name = rule_name
        self.enabled = enabled
        self.hits = hits
        self.sources = list()
        self.destinations = list()
        self.services = list()
        
