import requests
import json
from .query_machine import QueryMachine
from geopandas import *
import geocoder

API_KEY = ''    #PUSHA EJ TILL GIT

def get_current_location():
    location = geocoder.ip('me')
    return location.latlng  

def get_latlon_from_location(search_string: str) -> tuple: #Returnerar tuple med latlon från arbiträr search string. 
    res = geopandas.tools.geocode("Umeå") # Search_string vara formatterad lite hursomhelst till min förståelse.
    lon = res.get_coordinates().iat[0, 0]
    lat = res.get_coordinates().iat[0, 1]
    return (lat, lon)

# Places API 
base_url_nearby = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

# Place Details API
base_url_details = 'https://maps.googleapis.com/maps/api/place/details/json'

query=QueryMachine()


def json_file_to_database(path):
    with open(path, encoding="utf-8") as file:
        data = json.load(file)
    for place in data.values():
        place_id = place["place_id"]
        farms_to_database(place_id, place)


        

def farms_to_database(id, dict):
    if dict['business_status'] == 'OPERATIONAL':

        #finns ingen description i API-resultatet troligtvis, har dock kvar den så länge
        query.add_location(id,dict['name'],'No description available',dict['rating'],dict['geometry']['location']['lat'],
            dict['geometry']['location']['lng'],dict['formatted_address'],dict['website'],dict['international_phone_number'])
        
        if dict['wheelchair_accessible_entrance'] != None:
            query.add_farmtag(id, 'wheelchair')
        if dict['open_now'] != None:
            query.add_farmtag(id, 'open_now')
        if dict['opening_hours'] != None:
            for day in range(len(dict['opening_hours']["periods"])):
                cur_day = dict['opening_hours']["periods"][day]
                if 'close' in cur_day and 'open' in cur_day:
                    query.add_opening_hours(id,cur_day['open']['day'],cur_day['open']['time'], cur_day['close']['time'])




# Funkar bara på sverige nu eftersom man behöver andra keywords för att hitta bongårdar i andra länder. Alltså det respektive landets översättning av "bondgård" exempelvis.
def local_farms_sweden(latitude: float,longitude:float, radius: float = 50000):
    params_nearby = {
        'key': API_KEY,
        'location': f"{latitude},{longitude}",
        'radius': f'{radius}',  # Meter
        'keyword': 'gårdsbutik',
        'region': 'SE'
        #'keyword': 'gårdsbutik' funkar rätt bra, byta?

    }

    include_fields = ["name", "business_status", "formatted_address", "international_phone_number", "geometry", "rating", "url", "website", "wheelchair_accessible_entrance","open_now", "opening_hours"]
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
                all_farms[farm_name] = included_farm_details   #onödigt bara under develop-fasen  

                farms_to_database(place_id, included_farm_details)
                
            else:
                print('Error:', response_details.status_code)
                
    else:
        print('Error:', response_nearby.status_code)

    with open('all_API_data_temp.json', 'w', encoding='utf-8') as json_file:    #Denna JSON innehåller ALL info från API-resultatet
        json.dump(all_farms, json_file, indent=4, ensure_ascii=False)

def local_farms_startingpoint():
    local_farms_sweden(get_current_location()[0], get_current_location()[1])
