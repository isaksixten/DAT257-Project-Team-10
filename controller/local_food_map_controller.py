# controller/local_food_map_controller.py

from view.local_food_map_view import LocalFoodMapView
import model.farm_factories  # Assuming all factories are defined here

class LocalFoodMapController:
    def __init__(self):
        self.view = LocalFoodMapView()
        self.farm = None

    def create_farm(self, farm_type, name, location, description):
        factory_class_name = farm_type.capitalize() + "FarmFactory"
        factory_class = getattr(model.farm_factories, factory_class_name, None)

        if factory_class:
            factory = factory_class()
            self.farm = factory.create_farm(name, location, description)
        else:
            print("Unknown farm type")
            self.farm = None

    def display_farm(self):
        if self.farm is not None:
            self.view.display_farm(self.farm)
        else:
            print("No farm to display")
