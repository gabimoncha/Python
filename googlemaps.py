import json
import geocoder
from security import safe_requests

g = geocoder.ip("me")

lat = g.latlng[0]

longi = g.latlng[1]
query = input("Enter the query")

key = "your_api_key"
url = (
    "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="
    + str(lat)
    + ","
    + str(longi)
    + "radius=1000"
)

r = safe_requests.get(url + "query=" + query + "&key=" + key)

x = r.json()
y = x["results"]
print(y)
