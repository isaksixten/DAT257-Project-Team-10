# controller/local_food_map_controller.py

from view.local_food_map_view import LocalFoodMapView
import model.farm_factories  # Assuming all factories are defined here

# controller/local_food_map_controller.py

class LocalFoodMapController:
    def __init__(self):
        self.farms = {}  # Stores farm objects, categorized by farm type
        self.view = LocalFoodMapView()

    def create_farm(self, farm_type, name, location, description):
        factory_class_name = farm_type.capitalize() + "FarmFactory"
        factory_class = getattr(model.farm_factories, factory_class_name, None)
        if factory_class:
            factory = factory_class()
            farm = factory.create_farm(name, location, description)
            # Store the created farm in the dictionary
            if farm_type not in self.farms:
                self.farms[farm_type] = []
            self.farms[farm_type].append(farm)
        else:
            print("Unknown farm type")

    def display_farms(self):
        for farm_type, farms in self.farms.items():
            for farm in farms:
                self.view.display_farm(farm)
