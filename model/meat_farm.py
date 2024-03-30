from .I_farm import FarmInterface


class MeatFarm(FarmInterface):
    def __init__(self, name, location, description, latitude, longitude):
        self.name = name
        self.location = location
        self.description = description
        self.farm_type = "meat"
        self.latitude = latitude
        self.longitude = longitude
        self.id = None

    def get_details(self):
        return f"Meat Farm: {self.name}, located at {self.location}. {self.description}, {self.latitude}, {self.longitude}"

    @staticmethod
    def create(name, location, description, latitude, longitude):
        return MeatFarm(name, location, description, latitude, longitude)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'farm_type': self.farm_type,
            'description': self.description,
            'latitude': self.latitude,
            'longitude': self.longitude
        }
