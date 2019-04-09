import copy

class CpPolicySection:
    def __init__(self, section_uid, section_name):
        self.uid = section_uid
        self.name = section_name
        self.rules = list()