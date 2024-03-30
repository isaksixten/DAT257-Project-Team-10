# controller/local_food_map_controller.py

from view.local_food_map_view import LocalFoodMapView
import model.farm_factories  # Assuming all factories are defined here
# controller/local_food_map_controller.py

from model.factory_registry import FactoryRegistry

class LocalFoodMapController:
    def __init__(self, view):
        self.view = view
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

    def display_home_page(self):
        # Call the view to render the home page
        return self.view.render_home_page(self.get_all_farms())

    def display_farm_page(self, farm_id):
        # Fetch the specific farm, then call the view to render the farm page
        farm = self.get_farm_by_id(farm_id)
        if farm:
            return self.view.render_farm_page(farm)
        else:
            return self.view.render_error("Farm not found")

    def get_farm_by_id(self, farm_id):
        # Search through the list of farm dictionaries for the one with the matching id
        farm_dict = next((farm.to_dict() for farm in self.farms if farm.id == farm_id), None)
        return farm_dict
