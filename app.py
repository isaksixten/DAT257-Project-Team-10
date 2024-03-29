from flask import Flask, render_template, request, redirect, url_for
from controller.local_food_map_controller import LocalFoodMapController

app = Flask(__name__)

# Initialize the controller
controller = LocalFoodMapController()

# Create farms as specified
controller.create_farm("vegetable", "Green Thumb", "Valley Region", "Specializes in organic vegetables", -37.33056, 48.64247)
controller.create_farm("meat", "Meat Lovers", "Gothenburg", "Specializes in meat, that you love!", 44.91770, -122.68503)
controller.create_farm("meat", "Meat Dominators", "Linköping", "Serves dominant meat such as snakes!", 23.63305, 147.51138)

@app.route('/')
def home():
    # Use controller.get_all_farms() to get the farm details for the form
    farms = controller.get_all_farms()
    return render_template('index.html', farms=farms)

@app.route('/show_farm', methods=['POST'])
def show_farm():
    farm_id = request.form.get('farm_id')
    # Convert farm_id to int for comparison, as it's stored as int in the farms
    selected_farm = next((farm for farm in controller.get_all_farms() if farm['id'] == int(farm_id)), None)
    if not selected_farm:
        return redirect(url_for('home'))  # Redirect to home if farm is not found
    return render_template('show_farm.html', farm=selected_farm)


if __name__ == "__main__":
    app.run(debug=True)

