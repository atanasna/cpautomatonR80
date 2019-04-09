import copy

class CpPolicyLayer:
    def __init__(self, layer_uid, layer_name):
        self.uid = layer_uid
        self.name = layer_name
        self.sections = list()