import random

class Model:
    def __init__(self):
        self._cost = random.uniform(0.0, 10.0)
        pass
    def getCost(self):
        pass
    def setCost(self, value):
        if value <= 0:
            return
        
        self._cost = value
    cost = property(getCost,setCost)

