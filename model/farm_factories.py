from .vegetable_farm import VegetableFarm
from .I_farm import FarmFactory
from .meat_farm import MeatFarm

class VegetableFarmFactory(FarmFactory):
    def create_farm(self, name, location, description):
        return VegetableFarm(name, location, description)


class MeatFarmFactory(FarmFactory):
    def create_farm(self, name, location, description):
        return MeatFarm(name, location, description)
