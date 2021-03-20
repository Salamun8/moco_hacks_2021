# import requests

# g_api_key = "AIzaSyA592HwCkixwp7W8zRekEf2NZuyfKZNfvc"

def address_formatter(address, city, state, zip_code):
    # Ex: "1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA"
    # Make sure state is just 2 letters!
    formatted_address = (address + ", " + city + ", " + state + " " + zip_code + ", USA")
    return formatted_address

# def get_lat_long_locType(input_address):
def get_lat_long_locType(google_api_key, address, city, state, zip_code):
    input_address = address_formatter(address, city, state, zip_code)

    lat = None
    long = None
    locType = None
    place_id = None
    status = None
    api_key = google_api_key
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{base_url}?address={input_address}&key={api_key}"

    r = requests.get(endpoint)

    if r.status_code not in range(200, 299):
        return [None, None, None]
    
    try:
        json_file = r.json()
        results = json_file["results"][0]
        lat = results["geometry"]["location"]["lat"]
        long = results["geometry"]["location"]["lng"]
        # locType = results["geometry"]["location_type"]
        # Default Place type, since not using Places API
        locType = "shopping_mall"
        place_id = results["place_id"]
        status = json_file["status"]

        # NON-ERRORS:
        # "OK" indicates that no errors occurred; the address was successfully parsed and at least one geocode was returned
        if (status == "OK"):
            return [lat, long, locType, place_id]
        
        # "ZERO_RESULTS" indicates that the geocode was successful but returned no results. This may occur if the geocoder was passed a non-existent address
        elif (status == "ZERO_RESULTS"):
            return [status, status, status, status]
        

        # ERRORS:
        # "REQUEST_DENIED" indicates that your request was denied.
        elif (status == "REQUEST_DENIED"):
            return [status, status, status, status]
        
        # "INVALID_REQUEST" generally indicates that the query (address, components or latlng) is missing.
        elif (status == "INVALID_REQUEST"):
            return [status, status, status, status]
        
        # "UNKNOWN_ERROR" indicates that the request could not be processed due to a server error. The request may succeed if you try again.
        elif (status == "UNKNOWN_ERROR"):
            return [status, status, status, status]

    except:
        print("Something has gone wrong!")
        # Pass: https://www.google.com/search?q=pass+python+function&rlz=1C1SQJL_enUS806US806&oq=pass+python&aqs=chrome.2.69i57j0l6j69i65.2918j0j1&sourceid=chrome&ie=UTF-8 
        pass
        return [None, None, None]

def master_geocoding(google_api_key, address, city, state, zip_code):
    return get_lat_long_locType(google_api_key, address, city, state, zip_code)

# Tester Code
# print(master_geocoding(g_api_key, "10804 Brewer House Road", "Rockville", "MD", "20852"))
# print(master_geocoding(g_api_key, "6400 Rock Spring Dr", "Bethesda", "MD", "20814"))