from abc import ABC, abstractmethod

class FarmInterface(ABC):
    @abstractmethod
    def get_details(self):
        pass

    @staticmethod
    @abstractmethod
    def create(name, location, description):
        pass

class FarmFactory(ABC):
    @abstractmethod
    def create_farm(self, name, location, description):
        pass

    def render(self, name, location, description):
        farm = self.create_farm(name, location, description)
        print(f"Rendering farm: {farm.get_details()}")