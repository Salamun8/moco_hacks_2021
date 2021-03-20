import requests



google_api_key = "AIzaSyA592HwCkixwp7W8zRekEf2NZuyfKZNfvc"

def address_formatter(address, city, state, zip_code):
    # Ex: "1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA"
    # Make sure state is just 2 letters!
    formatted_address = (address + ", " + city + ", " + state + " " + zip_code + ", USA")
    return formatted_address

# def get_lat_long_locType(input_address):
def get_lat_long_locType(address, city, state, zip_code):
    input_address = address_formatter(address, city, state, zip_code)

    lat = None
    long = None
    locType = None
    api_key = google_api_key
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{base_url}?address={input_address}&key={api_key}"

    r = requests.get(endpoint)

    if r.status_code not in range(200, 299):
        return [None, None, None]
    
    try:
        results = r.json()["results"][0]
        lat = results["geometry"]["location"]["lat"]
        long = results["geometry"]["location"]["lng"]
        # locType = results["geometry"]["location_type"]
        # Default Place type, since not using Places API
        locType = "shopping_mall"
        return [lat, long, locType]

        # NEED TO CREATE IF STATEMENTS FOR THE STUFF BELOW!!!
        # status = ["status"]
        # NON-ERRORS:
        # "OK" indicates that no errors occurred; the address was successfully parsed and at least one geocode was returned
        # "ZERO_RESULTS" indicates that the geocode was successful but returned no results. This may occur if the geocoder was passed a non-existent address

        # ERRORS:
        # "REQUEST_DENIED" indicates that your request was denied.
        # "INVALID_REQUEST" generally indicates that the query (address, components or latlng) is missing.
        # "UNKNOWN_ERROR" indicates that the request could not be processed due to a server error. The request may succeed if you try again.
    
    except:
        print("Something has gone wrong!")
        return [None, None, None]
        # Pass: https://www.google.com/search?q=pass+python+function&rlz=1C1SQJL_enUS806US806&oq=pass+python&aqs=chrome.2.69i57j0l6j69i65.2918j0j1&sourceid=chrome&ie=UTF-8 
        pass

print(get_lat_long_locType("10804 Brewer House Road", "Rockville", "MD", "20852"))
# IT WORKSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS