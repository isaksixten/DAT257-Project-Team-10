# app.py
from controller.local_food_map_controller import LocalFoodMapController


def main():
    controller = LocalFoodMapController()
    controller.create_farm("vegetable", "Green Thumb", "Valley Region", "Specializes in organic vegetables")
    controller.create_farm("meat", "Meat Lovers", "Gothenburg", "Specializes in meat, that you love!")
    controller.display_farms()


if __name__ == "__main__":
    main()
