import requests
import json

API_KEY = 'AIzaSyBrVEi0F4Taz3Z80w5xgcYvKbeq5lJ53kw'

# Places API 
base_url_nearby = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

# Place Details API
base_url_details = 'https://maps.googleapis.com/maps/api/place/details/json'

# Funkar bara på sverige nu eftersom man behöver andra keywords för att hitta bongårdar i andra länder. Alltså det respektive landets översättning av "bondgård" exempelvis.
def local_farms_sweden(longitude, latitude):
    params_nearby = {
        'key': API_KEY,
        'location': f"{longitude},{latitude}",
        'radius': '5000',  # Meter
        'keyword': 'bondgård'  
    }

    include_fields = ["name", "business_status", "formatted_address", "formatted_phone_number", "geometry", "rating", "url", "website", "wheelchair_accessible_entrance"]

    all_farms = {}

    response_nearby = requests.get(base_url_nearby, params=params_nearby)

    if response_nearby.status_code == 200:
        data_nearby = response_nearby.json()
        
        for place in data_nearby['results']:
            place_id = place['place_id']

            params_details = {
                'key': API_KEY,
                'place_id': place_id
            }
            
            response_details = requests.get(base_url_details, params=params_details)

            if response_details.status_code == 200:
                data_details = response_details.json()
                
                farm_details = data_details['result']
                
                included_farm_details = {field: farm_details.get(field, None) for field in include_fields}
                    
                farm_name = included_farm_details.get('name', 'Unnamed Farm')
                all_farms[farm_name] = included_farm_details
            else:
                print('Error:', response_details.status_code)
    else:
        print('Error:', response_nearby.status_code)

    with open('farm_data_temp.json', 'w', encoding='utf-8') as json_file:
        json.dump(all_farms_by_name, json_file, indent=4, ensure_ascii=False)
local_farms_sweden(59.334591, 18.063240)