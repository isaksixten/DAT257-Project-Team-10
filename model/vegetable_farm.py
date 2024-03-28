from .I_farm import FarmInterface

class VegetableFarm(FarmInterface):
    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description

    def get_details(self):
        return f"Vegetable Farm: {self.name}, located at {self.location}. {self.description}"

    @staticmethod
    def create(name, location, description):
        return VegetableFarm(name, location, description)