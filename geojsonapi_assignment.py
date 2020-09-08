import urllib.request, urllib.parse, urllib.error
import json

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'


address = input('Enter location: ')


url = serviceurl + urllib.parse.urlencode({'address': address, 'key': api_key})

print('Retrieving', url)

u_handle = urllib.request.urlopen(url)
data = u_handle.read().decode()
#print("Data: ", data)
print('Retrieved', len(data), 'characters')

js = json.loads(data)

place_id = js["results"][0]["place_id"]
print('Place id', place_id)
