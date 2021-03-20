import geocoding as gc
# import populartimes
import livepopulartimes

g_api_key = "AIzaSyA592HwCkixwp7W8zRekEf2NZuyfKZNfvc"

def master_at_location(google_api_key, address, city, state, zip_code):
    geo_data = gc.master_geocoding(google_api_key, address, city, state, zip_code)
    latitude = geo_data[0]
    longitude = geo_data[1]
    location_type = geo_data[2]
    place_id = geo_data[3]

    raw_risk_data = populartimes.get_id(google_api_key, place_id)["populartimes"]

    return raw_risk_data


# testing code
# print(gc.master_geocoding(g_api_key, "10804 Brewer House Road", "Rockville", "MD", "20852"))
# 7101 Democracy Blvd, Bethesda, MD 20817
print(master_at_location(g_api_key, "7101 Democracy Blvd", "Bethesda", "MD", "20817"))