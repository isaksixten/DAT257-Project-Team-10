from .I_geo_strategies import GeolocationStrategy
import requests

class CityNameGeolocation(GeolocationStrategy):
    class CityNameGeolocation(GeolocationStrategy):
        def get_coordinates(self, city_name):
            API_URL = "https://nominatim.openstreetmap.org/search"
            params = {
                'q': city_name,
                'format': 'json',
                'limit': 1
            }
            response = requests.get(API_URL, params=params)
            if response.status_code == 200:
                results = response.json()
                if results:
                    # Extracting the first result as the most relevant match
                    latitude = results[0]['lat']
                    longitude = results[0]['lon']
                    return float(latitude), float(longitude)
                else:
                    raise ValueError(f"No coordinates found for {city_name}")
            else:
                raise Exception(f"Failed to fetch coordinates for {city_name}")

class DirectInputGeolocation(GeolocationStrategy):
    def get_coordinates(self, coordinates):
        # Directly use the provided coordinates
        return coordinates

class MapClickGeolocation(GeolocationStrategy):
    def get_coordinates(self, map_data):
        # Extract coordinates from map data where user clicked
        pass