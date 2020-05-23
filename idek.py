import urllib.request
import json
endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
api_key = 'AIzaSyCCQdTm0Fyau11GLhWAqr83ZLVdUBOklME'
origin = input('Where are you?: ').replace(' ','+')
destination = input('Where you wanna go?: ')

nav_request = 'origin={}&destinationd={}&key={}'.format(origin, destination, api_key)
request = endpoint + nav_request
response = urllib.request.urlopen(request).read()
directions = json.loads(response)
print(directions)