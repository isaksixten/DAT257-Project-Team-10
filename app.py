# app.py

from flask import Flask, request, redirect, url_for
from backend.local_food_map_controller import LocalFoodMapController
from frontend.local_food_map_view import LocalFoodMapView
from backend.query_machine import QueryMachine

app = Flask(__name__)

# Initialize the controller
view = LocalFoodMapView
controller = LocalFoodMapController(view)

# Create farms as specified
#controller.create_farm("vegetable", "Green Thumb", "Valley Region", "Specializes in organic vegetables", -37.33056, 48.64247)
#controller.create_farm("meat", "Meat Lovers", "Gothenburg", "Specializes in meat, that you love!", 44.91770, -122.68503)
#controller.create_farm("meat", "Meat Dominators", "Linköping", "Serves dominant meat such as snakes!", 23.63305, 147.51138)

@app.route('/')
def home():
    # Call controller to display the home page
    return controller.display_home_page()

@app.route('/show_farm', methods=['POST'])
def show_farm():
    # Retrieve farm ID from form data
    farm_id = request.form.get('farm_id', type=int)
    # Call controller to display the farm page
    return controller.display_farm_page(farm_id)

@app.route('/fetch-tags') 
def fetch_tags(): 
    return controller.get_farm_tags() 


if __name__ == "__main__":
    app.run(debug=True)
