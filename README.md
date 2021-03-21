# **moco_hacks_2021**
# **Corona-Safe**
#
# **FILE STRUCTURE BREAKDOWN**
1. Final Product:
    - `final_product` --> `coronasafe.py`
        - Contains all the code for the project, including GUI
            - This is because importing other python files and external functions is difficult in Tkinter.
2. Foot Traffic Backend (not run in final product):
    - `backend` --> `foot_traffic` --> `foot_traffic.py`
        - Contains all code for foot traffic processing & geocoding.
    - `backend` --> `foot_traffic` --> `geocoding.py`
        - Contains all code for geocoding.
#
# **DOCUMENTATION**
## **Main Groups**
1. COVID-19 risk calculator based on an input address
    - Libraries used: `datetime`, and `requests`
    - Parameters: `google_api_key, address, city, state, zip_code, search_radius`
        - state needs to be formatted in their 2-letter, all caps format
        - Sample parameters (for the Empire State Building): `g_api_key, "20 W 34th St", "New York", "NY", "10001", radius`
            - NOTE: the default value for radius is set to 0.5 (miles)
    - functionality breakdown:
        - Uses address fields from user to generate a formatted address: `address_formatter(address, city, state, zip_code)`
        - The formatted address is geocoded using the Google Geocoding API: `master_geocoding(google_api_key, address, city, state, zip_code)`
            - A json request is made to access the Google Geocoding API
            - The latitude and longitude of the address is stored
        - A radius is then traced around the geocoded coordinates, and a list of (up to 20) nearby locations is extracted using the Google Places API: `key_buildings_search(google_api_key, address, city, state, zip_code, search_radius)`
            - A json request is made to access the Google Geocoding API
            - Each item in the list contains a types metadata
                - This is checked against a list of important types that signify a location that usually has a lot of people, and the total number of important locations is stored
        - The raw number from c.ii. is taken and multiplied by a weight relative to the current hour of day before being divided by the maximum time-weighted and multiplied by 100 to get a scale of risk from 0-100: `risk_rating_scaler(google_api_key, address, city, state, zip_code, search_radius)`
            - Weightage approximates typical times when people are the busiest on a  0.0-1.0 scale
        - The 100 scale is divided in thirds to output a low, medium, or high risk level that is returned to be turned into a visual representation in the GUI: `risk_rating_scaler(google_api_key, address, city, state, zip_code, search_radius) & tkinter GUI code`
            - Sample function call (for the Empire State Building): `risk_rating_scaler(g_api_key, "20 W 34th St", "New York", "NY", "10001", radius)`
