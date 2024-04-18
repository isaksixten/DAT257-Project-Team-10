import requests
import json

# Your API key
API_KEY = 'AIzaSyBrVEi0F4Taz3Z80w5xgcYvKbeq5lJ53kw'

# Base URL for the Places API nearby search
base_url_nearby = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

# Base URL for the Place Details API
base_url_details = 'https://maps.googleapis.com/maps/api/place/details/json'

# Parameters for the nearby search request
params_nearby = {
    'key': API_KEY,
    'location': '57.65893,12.11792',  # Latitude and longitude of the location you want to search around
    'radius': '5000',  # Search radius in meters (adjust as needed)
    'keyword': 'bondgård'  # Keyword to search for farms
}

# Make the nearby search request
response_nearby = requests.get(base_url_nearby, params=params_nearby)

# Process the nearby search response
if response_nearby.status_code == 200:
    data_nearby = response_nearby.json()
    print("Nearby Search Response:", data_nearby)  # Debugging: Print the nearby search response
    
    # Iterate over each farm in the nearby search results
    for place in data_nearby['results']:
        # Get the place ID of the farm
        place_id = place['place_id']
        print("Place ID:", place_id)  # Debugging: Print the place ID
        
        # Parameters for the Place Details API request
        params_details = {
            'key': API_KEY,
            'place_id': place_id
        }
        
        # Make the Place Details API request
        response_details = requests.get(base_url_details, params=params_details)
        print("Place Details API Request URL:", response_details.url)  # Debugging: Print the request URL
        
        # Process the Place Details API response
        if response_details.status_code == 200:
            data_details = response_details.json()
            print("Place Details Response:", data_details)  # Debugging: Print the place details response
            
            # Extract additional information about the farm
            farm_details = data_details['result']
            print("Farm Details:", farm_details)  # Print the details of the farm
            with open('farm_data_temp.json', 'w', encoding = 'utf-8') as json_file:
                json.dump(farm_details, json_file, indent=4, ensure_ascii=False)
        else:
            print('Error:', response_details.status_code)
else:
    print('Error:', response_nearby.status_code)
