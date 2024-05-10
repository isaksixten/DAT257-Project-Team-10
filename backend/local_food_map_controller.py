# controller/local_food_map_controller.py
# controller/local_food_map_controller.py

from backend.query_machine import QueryMachine
from frontend.local_food_map_view import LocalFoodMapView
from backend.APItest import local_farms_sweden, local_farms_startingpoint


class LocalFoodMapController:
    def __init__(self, view):
        self.view : LocalFoodMapView = view
        self.query_machine=QueryMachine()  # Use FarmModel to manage farms
        self.geolocation_strategy = None

    def create_farm(self, name, description, latitude, longitude):
        try:
            self.query_machine.add_location(self.query_machine.id_generator(), name, description, latitude, longitude)
        except ValueError as e:
            print(e)

    def display_home_page(self):
        local_farms_startingpoint()
        farms = self.query_machine.fetch_all_locations()
        return self.view.render_home_page(farms)

    def update_locations_from_search(self,lon,lat):
        local_farms_sweden(lon,lat)

    def fetch_farms(self):
        return self.query_machine.fetch_all_locations()

    def display_farm_page(self, farm_id):
        farm = self.query_machine.fetch_location(farm_id)
        if farm:
            return self.view.render_farm_page(farm)
        else:
            return self.view.render_not_found("Farm not found")


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

    def get_tags(self):
        tags=self.query_machine.fetch_tags()
        return tags

    def get_farmtags(self):
        farmtags=self.query_machine.fetch_farmtags()
        return farmtags

    def get_search_options(self,term):
        results=self.query_machine.fetch_by_search(term)
        return results