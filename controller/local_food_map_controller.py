# controller/local_food_map_controller.py

from view.local_food_map_view import LocalFoodMapView
import model.farm_factories  # Assuming all factories are defined here
# controller/local_food_map_controller.py

from model.factory_registry import FactoryRegistry

class LocalFoodMapController:
    def __init__(self):
        self.farms = []  # This will store farm objects
        self.next_id = 1  # Initialize a counter for assigning IDs

    def create_farm(self, farm_type, name, location, description, latitude, longitude):
        try:
            factory = FactoryRegistry.get_factory(farm_type)
            farm = factory.create_farm(name, location, description, latitude, longitude)
            farm.id = self.next_id  # Assign an ID to the farm
            self.next_id += 1  # Increment the ID counter for the next farm
            self.farms.append(farm)
        except ValueError as e:
            print(e)

    def get_all_farms(self):
        # Assuming each farm object has a to_dict method to convert it to dictionary
        return [farm.to_dict() for farm in self.farms]
