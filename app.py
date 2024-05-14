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

@app.route('/new-farms', methods=["POST"])
def api_ping():
    lat = request.args.get('lat')  # Get the 'lon' parameter from the request
    lon = request.args.get('lon')  # Get the 'lat' parameter from the request
    controller.update_locations_from_search(lat, lon)
    return 'Success', 200  # Return a success message with status code 200

@app.route('/fetch-farms')
def fetch_farms():
    return controller.fetch_farms()

@app.route('/show_farm', methods=['POST'])
def show_farm():
    # Retrieve farm ID from form data
    farm_id = request.form.get('farm_id', type=int)
    # Call controller to display the farm page
    return controller.display_farm_page(farm_id)

@app.route('/fetch-tags') 
def fetch_tags(): 
    return controller.get_tags() 

@app.route('/fetch-search-options', methods=['POST'])
def fetch_search_options():
    data = request.get_json()  # Get the JSON data from the request
    term = data.get('term', '')  # Extract the search term from the JSON data
    return controller.get_search_options(term)

@app.route('/fetch-farms-with-tags',methods=["POST"])
def fetch_continous_farmtags():
    data = request.get_json()
    tags = data.get('tags', [])
    return controller.get_farmtags(tags)

if __name__ == "__main__":
    app.run(debug=True)
    
