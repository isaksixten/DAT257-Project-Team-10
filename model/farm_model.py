# model/farm_model.py
from distance_calculator import DistanceCalculator

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

    def get_farms_sorted_by_distance(self, user_lat, user_lon):
        # Calculate the distance for each farm and add it as a new key-value pair
        for farm in self.farms:
            farm['distance'] = DistanceCalculator.calculate_distance(
                user_lat, user_lon, farm['latitude'], farm['longitude'])

        # Sort the farms by the calculated distance
        sorted_farms = sorted(self.farms, key=lambda farm: farm['distance'])

        return sorted_farms




