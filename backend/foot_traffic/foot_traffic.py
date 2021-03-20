import requests
import geocoding as gc

g_api_key = "AIzaSyA592HwCkixwp7W8zRekEf2NZuyfKZNfvc"

print(gc.master_geocoding(g_api_key, "10804 Brewer House Road", "Rockville", "MD", "20852"))