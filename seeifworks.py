import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://python-data.dr-chuck.net/geojson?"
# This API only accepts the university in a list of its accepted ones.
# This API uses the same parameters (sensor and address) as the Google API.
# This API also has no rate limit so you can test as often as you like.
# If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.

address_input = input("Enter location: ")
params = {"sensor": "false", "address": address_input}
url = serviceurl + urllib.parse.urlencode(params)
print("Retrieving ", url)
data = urllib.request.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

place_id = json_obj["results"][0]["place_id"]
print("Place id", place_id)
