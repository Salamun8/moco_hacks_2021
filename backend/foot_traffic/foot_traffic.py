import geocoding as gc
# import populartimes
# import livepopulartimes
import datetime as dt
import requests

g_api_key = "AIzaSyA592HwCkixwp7W8zRekEf2NZuyfKZNfvc"
radius = 0.5


def key_buildings_search(google_api_key, address, city, state, zip_code, search_radius):
    search_results = None
    important_types = ["airport", "amusement_park", "aquarium", "art_gallery", "bank", "casino", "clothing_store", 
    "convenience_store", "department_store", "drugstore", "movie_theater", "museum", "park", "pharmacy", "restaurant", "shopping_mall", "stadium", 
    "store", "subway_station", "supermarket", "tourist_attraction", "zoo", "lodging"]

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
            is_important = False
            already_true = False
            types_length = len(search_results[i]["types"])
            k = 0
            # while ((k < types_length) and (already_true == False)):
            while ((k < types_length) and (already_true == False)):
                if(search_results[i]["types"][k] in important_types):
                    is_important = True
                    already_true = True
                    # final_number = final_number + 1
                else:
                    is_important = False
                
                print(search_results[i]["types"][k])
                k = k + 1
            if((already_true == True)):
                final_number = final_number + 1
            
            print(search_results[i]["types"])
            print(is_important)
            print(already_true)
            # is_important = False
            # already_true = False
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

def risk_rating_scaler(google_api_key, address, city, state, zip_code, search_radius):
    try:
        # ONLY BECAUSE KEY_BUILDINGS_SEARCH IS TEMPORARILY RETURNING 2 VALUES!!!
        raw_value = int(key_buildings_search(google_api_key, address, city, state, zip_code, search_radius)[1])
        current_hour = int(dt.datetime.now().hour)
        time_weights = {
            0: 0.2,
            1: 0.1,
            2: 0.1,
            3: 0.1,
            4: 0.1,
            5: 0.2,
            6: 0.3,
            7: 0.4,
            8: 0.5,
            9: 0.5,
            10: 0.5,
            11: 0.6,
            12: 0.6,
            13: 0.7,
            14: 0.7,
            15: 1.0,
            16: 1.0,
            17: 1.0,
            18: 0.8,
            19: 0.8,
            20: 0.8,
            21: 0.5,
            22: 0.5,
            23: 0.2
        }
        max = 20 * 1.0
        weighted_value = ((raw_value * time_weights[current_hour])/max) * 100
        print(raw_value)
        print("current hour: " + str(current_hour))
        print(weighted_value)
        if(weighted_value < 33.33):
            return "low"
        elif(weighted_value < 66.66):
            return "medium"
        elif(weighted_value <= 100):
            return "high"
        else:
            return "Error"
    except:
        return "Error"



# testing code
# 10804 Brewer House Road, Rockville, MD 20852
    # [20,20]
# 7101 Democracy Blvd, Bethesda, MD 20817
# 285 Fulton St, New York, NY 10007
# print(master_at_location(g_api_key, "22 Warren St", "New York", "NY", "10007"))
print(risk_rating_scaler(g_api_key, "285 BigTitty St", "New York", "NY", "1007", radius))
# print(key_buildings_search(g_api_key, "10804 Brewer House Road", "Rockville", "MD", "20852", radius))

geo_data = gc.master_geocoding(g_api_key, "285 BigTitty St", "Bew York", "NZ", "10342432007")
latitude = geo_data[0]
longitude = geo_data[1]
print(latitude, longitude)