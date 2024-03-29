from .vegetable_farm import VegetableFarm
from .I_farm import FarmFactory
from .meat_farm import MeatFarm
from .factory_registry import FactoryRegistry

class VegetableFarmFactory(FarmFactory):
    def create_farm(self, name, location, description, latitude, longtitude):
        return VegetableFarm(name, location, description, latitude, longtitude)

FactoryRegistry.register_factory("vegetable", VegetableFarmFactory)
class MeatFarmFactory(FarmFactory):
    def create_farm(self, name, location, description, latitude, longitude):
        return MeatFarm(name, location, description, latitude, longitude)

FactoryRegistry.register_factory("meat", MeatFarmFactory)