import copy

class CpPolicyPackage:
    def __init__(self, package_uid, package_name):
        self.uid = package_uid
        self.name = package_name
        self.access_enabled = False
        self.nat_enabled = False
        self.thread_enabled = False
        self.layers = list()