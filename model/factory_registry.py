# model/factory_registry.py

class FactoryRegistry:
    factories = {}

    @classmethod
    def register_factory(cls, farm_type, factory):
        cls.factories[farm_type] = factory

    @classmethod
    def get_factory(cls, farm_type):
        factory_class = cls.factories.get(farm_type)
        if not factory_class:
            raise ValueError(f"No factory registered for farm type '{farm_type}'")
        return factory_class()
