import geocoding as gc
# import populartimes
import livepopulartimes

import requests

g_api_key = "AIzaSyA592HwCkixwp7W8zRekEf2NZuyfKZNfvc"

def master_at_location(google_api_key, address, city, state, zip_code):
    geo_data = gc.master_geocoding(google_api_key, address, city, state, zip_code)
    latitude = geo_data[0]
    longitude = geo_data[1]
    location_type = geo_data[2]
    place_id = geo_data[3]

    # raw_risk_data = populartimes.get_id(google_api_key, place_id)["populartimes"]
    formatted_address = gc.address_formatter(address, city, state, zip_code)
    formatted_address = "(Gran Morsi) " +formatted_address

    # raw_risk_data = livepopulartimes.get_populartimes_by_address(formatted_address)["current_popularity"]
    raw_risk_data = livepopulartimes.get_populartimes_by_PlaceID(google_api_key, place_id)

    return raw_risk_data


def key_buildings_search(google_api_key, address, city, state, zip_code, search_radius):
    search_results = None
    important_types = ["airport", "amusement_park", "aquarium", "art_gallery", "bank", "casino", "clothing_store", 
    "convenience_store", "department_store", "drugstore", "electronics_store", "furniture_store", "hardware_store", 
    "home_goods_store", "movie_theater", "museum", "park", "pharmacy", "restaurant", "shopping_mall", "stadium", 
    "store", "subway_station", "supermarket", "tourist_attraction", "zoo", "premise"]

    is_important = False
    radius = 1609.34 * search_radius
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    geo_data = gc.master_geocoding(google_api_key, address, city, state, zip_code)
    latitude = geo_data[0]
    longitude = geo_data[1]
    endpoint = f"{base_url}?location={latitude}, {longitude}&radius={str(radius)}&opennow&rankby=prominence&key={google_api_key}"

    r = requests.get(endpoint)

    if r.status_code not in range(200, 299):
        return None

    try:
        json_file = r.json()
        search_results = json_file["results"]
        raw_number = len(search_results)
        final_number = 0
        status = json_file["status"]

        i = 0
        k = 0
        already_true = False
        while (i<raw_number):
            types_length = len(search_results[i]["types"])
            k = 0
            while ((k < types_length) and (already_true == False)):
                if(search_results[i]["types"][k] in important_types):
                    is_important = True
                    if(already_true == False):
                        already_true = True
                    # final_number = final_number + 1
                else:
                    is_important = False
                
                print(search_results[i]["types"][k])
                k = k + 1
            if((already_true != False)):
                final_number = final_number + 1
            
            print(search_results[i]["types"])
            print(is_important)
            print(already_true)
            is_important = False
            already_true = False
            i = i + 1
            

        # NON-ERRORS:
        # "OK" indicates that no errors occurred; the address was successfully parsed and at least one geocode was returned
        if (status == "OK"):
            # return [final_number, search_results]
            return [raw_number, final_number]
        # "ZERO_RESULTS" indicates that the geocode was successful but returned no results. This may occur if the geocoder was passed a non-existent address
        elif (status == "ZERO_RESULTS"):
            return status
        

        # ERRORS:
        # "REQUEST_DENIED" indicates that your request was denied.
        elif (status == "REQUEST_DENIED"):
            return status
        
        # "INVALID_REQUEST" generally indicates that the query (address, components or latlng) is missing.
        elif (status == "INVALID_REQUEST"):
            return status
        
        # "UNKNOWN_ERROR" indicates that the request could not be processed due to a server error. The request may succeed if you try again.
        elif (status == "UNKNOWN_ERROR"):
            return status

    except:
        print("Something has gone wrong!")
        # Pass: https://www.google.com/search?q=pass+python+function&rlz=1C1SQJL_enUS806US806&oq=pass+python&aqs=chrome.2.69i57j0l6j69i65.2918j0j1&sourceid=chrome&ie=UTF-8 
        pass
        return None

# testing code
# 10804 Brewer House Road, Rockville, MD 20852
    # [20,20]
# 7101 Democracy Blvd, Bethesda, MD 20817
# 285 Fulton St, New York, NY 10007
# print(master_at_location(g_api_key, "22 Warren St", "New York", "NY", "10007"))
print(key_buildings_search(g_api_key, "285 Fulton St", "New York", "NY", "10007", 1))