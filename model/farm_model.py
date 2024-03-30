# model/farm_model.py

class FarmModel:
    def __init__(self):
        self.farms = []
        self.next_id = 1

    def add_farm(self, farm_type, name, location, description, latitude, longitude, factory_registry):
        factory = factory_registry.get_factory(farm_type)
        farm = factory.create_farm(name, location, description, latitude, longitude)
        farm.id = self.next_id
        self.next_id += 1
        self.farms.append(farm)

    def get_all_farms(self):
        return [farm.to_dict() for farm in self.farms]

    def get_farm_by_id(self, farm_id):
        return next((farm.to_dict() for farm in self.farms if farm.id == farm_id), None)
