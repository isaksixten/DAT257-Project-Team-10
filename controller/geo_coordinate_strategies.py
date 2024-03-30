from .I_geo_strategies import GeolocationStrategy

class CityNameGeolocation(GeolocationStrategy):
    def get_coordinates(self, city_name):
        # Logic to fetch coordinates by city name
        pass

class DirectInputGeolocation(GeolocationStrategy):
    def get_coordinates(self, coordinates):
        # Directly use the provided coordinates
        return coordinates

class MapClickGeolocation(GeolocationStrategy):
    def get_coordinates(self, map_data):
        # Extract coordinates from map data where user clicked
        pass