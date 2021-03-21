# **moco_hacks_2021**
# **COVID-Safe**
#
# **DOCUMENTATION**
#
## **Main Groups**
## 1. COVID-19 risk calculator based on an input address
####   a. Parameters: `google_api_key, address, city, state, zip_code, search_radius`
####       i. state needs to be formatted in their 2-letter, all caps format
####       ii. Sample parameters (for the Empire State Building):
####           `g_api_key, "20 W 34th St", "New York", "NY", "10001", radius`
####           NOTE: the default value for radius is set to 0.5 (miles)
####   b. functionality breakdown:
####       a. Uses address fields from user to generate a formatted address: `address_formatter(address, city, state, zip_code)`
####       b. The formatted address is geocoded using the Google Geocoding API: `master_geocoding(google_api_key, address, city, state, zip_code)`
####           i. A json request is made to access the Google Geocoding API
####           ii. The latitude and longitude of the address is stored
####       c. A radius is then traced around the geocoded coordinates, and a list of (up to 20) nearby locations is extracted using the Google Places API: `key_buildings_search(google_api_key, address, city, state, zip_code, search_radius)`
####           i. A json request is made to access the Google Geocoding API
####           ii. Each item in the list contains a types metadata
####               1. This is checked against a list of important types that signify a location that usually has a lot of people, and the total number of important 
####       d. The raw number from c.ii. is taken and multiplied by a weight relative to the current hour of day before being divided by the maximum time-weighted and multiplied by 100 to get a scale of risk from 0-100: `risk_rating_scaler(google_api_key, address, city, state, zip_code, search_radius)`
####           i. Weightage approximates typical times when people are the busiest on a  0.0-1.0 scale
####       e. The 100 scale is divided in thirds to output a low, medium, or high risk level that is turned into a visual representation in the GUI: `risk_rating_scaler(google_api_key, address, city, state, zip_code, search_radius) & tkinter GUI code`
