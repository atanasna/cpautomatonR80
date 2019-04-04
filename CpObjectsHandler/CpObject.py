#from abc import ABC, abstractmethod

class CpObject():
    # string: obj_name
    # string: obj_color
    def __init__(self, uid, name, color="Black"):
        self.uid = uid
        self.name = name
        self.color = color
        #super().__init__()
