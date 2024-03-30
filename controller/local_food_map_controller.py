# controller/local_food_map_controller.py

from view.local_food_map_view import LocalFoodMapView
import model.farm_factories  # Assuming all factories are defined here
# controller/local_food_map_controller.py

from model.farm_model import FarmModel
from model.factory_registry import FactoryRegistry

class LocalFoodMapController:
    def __init__(self, view):
        self.view = view
        self.model = FarmModel()  # Use FarmModel to manage farms
        self.geolocation_strategy = None

    def create_farm(self, farm_type, name, location, description, latitude, longitude):
        try:
            self.model.add_farm(farm_type, name, location, description, latitude, longitude, FactoryRegistry)
        except ValueError as e:
            print(e)

    def display_home_page(self):
        farms = self.model.get_all_farms()
        return self.view.render_home_page(farms)

    def display_farm_page(self, farm_id):
        farm = self.model.get_farm_by_id(farm_id)
        if farm:
            return self.view.render_farm_page(farm)
        else:
            return self.view.render_error("Farm not found")

    def get_farm_by_id(self, farm_id):
        # Search through the list of farm dictionaries for the one with the matching id
        farm_dict = next((farm.to_dict() for farm in self.farms if farm.id == farm_id), None)
        return farm_dict

    def set_geolocation_strategy(self, strategy):
        self.geolocation_strategy = strategy

    def get_coordinates_from_input(self, input_data):
        if self.geolocation_strategy:
            return self.geolocation_strategy.get_coordinates(input_data)
        else:
            raise ValueError("Geolocation strategy not set.")

    def display_farms_sorted_by_proximity(self, user_lat, user_lon):
        sorted_farms = self.model.get_farms_sorted_by_distance(user_lat, user_lon)
        return self.view.render_farms_sorted_page(sorted_farms)