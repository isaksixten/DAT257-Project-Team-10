import requests
import json
from query_machine import QueryMachine

API_KEY = 'AIzaSyD7Cig0vx07muhSrCE2Fo4EOcGpWvKH4Hk'    #PUSHA EJ TILL GIT

# Places API 
base_url_nearby = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

# Place Details API
base_url_details = 'https://maps.googleapis.com/maps/api/place/details/json'

query=QueryMachine()

def farms_to_database(id, dict):
    query.add_location(id,dict['name'],'empty',dict['geometry']['location']['lat'],
        dict['geometry']['location']['lng'],)

    if dict['website'] != None:
        query.add_farmtag(id, 'website')
    if dict['wheelchair_accessible_entrance'] != None:
        query.add_farmtag(id, 'wheelchair')
    if dict['rating'] != None:
        query.add_farmtag(id, 'rating')
    if dict['business_status'] == 'OPERATIONAL':
        query.add_farmtag(id, 'open')
                
    query.add_farm_info(id, dict['formatted_address']
                        , dict['international_phone_number']
                        , dict['rating']
                        , dict['website'])




# Funkar bara på sverige nu eftersom man behöver andra keywords för att hitta bongårdar i andra länder. Alltså det respektive landets översättning av "bondgård" exempelvis.
def local_farms_sweden(longitude: float, latitude: float, radius: float):
    params_nearby = {
        'key': API_KEY,
        'location': f"{longitude},{latitude}",
        'radius': f'{radius}',  # Meter
        'keyword': 'bondgård'  
    }

    include_fields = ["name", "business_status", "formatted_address", "international_phone_number", "geometry", "rating", "url", "website", "wheelchair_accessible_entrance","open_now"]
    #periods? (öppettider)
    all_farms = {}  #Onödig, bara under develop-fas

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
                all_farms[farm_name] = included_farm_details    #onödigt bara under develop-fasen

                farms_to_database(place_id, included_farm_details)
                
            else:
                print('Error:', response_details.status_code)
                
    else:
        print('Error:', response_nearby.status_code)

    with open('farm_data_temp.json', 'w', encoding='utf-8') as json_file:
        json.dump(all_farms, json_file, indent=4, ensure_ascii=False)
local_farms_sweden(59.334591, 18.063240, 5000)