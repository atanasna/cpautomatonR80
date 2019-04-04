from CpObject import *

class CpNetworkObject(CpObject):
    # string: obj_name
    # string: obj_color
    def __init__(self, uid, name, color="Black"):
        CpObject.__init__(self, uid, name, color)
        
    #@abstractmethod
    def ip_include(self, obj):
        pass

    def ip_equal(self, obj):
        pass