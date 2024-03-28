from .vegetable_farm import VegetableFarm
from .I_farm import FarmFactory

class VegetableFarmFactory(FarmFactory):
    def create_farm(self, name, location, description):
        return VegetableFarm(name, location, description)
