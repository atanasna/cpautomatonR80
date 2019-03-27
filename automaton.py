from CpObjectsHandler.CpObjectsHandler import *
from CpApiHandler.CpApiHandler import *
import json

class Automaton:
    def __init__(self):
        self.api = CpApiHandler("34.248.149.172", "king", "passport")
        self.objectsHandler = CpObjectsHandler()
        self.objectsHandler.load(self.api.get_net_objects())
        self.objectsHandler.print_objects()
        
a = Automaton()