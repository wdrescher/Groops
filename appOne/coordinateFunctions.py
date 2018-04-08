import requests

from math import sin, cos, sqrt, atan2, radians
from openpyxl import load_workbook, Workbook

# Calculate the distance between two geocode coordinates
def distance(coord1, coord2):
	R = 6373.0
	lat1 = radians(coord1[0])
	lon1 = radians(coord1[1])
	lat2 = radians(coord2[0])
	lon2 = radians(coord2[1])

	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
	c = 2 * atan2(sqrt(a), sqrt(1-a))
	distance = R * c
	return distance * 0.621371 # convert to miles

# convert address to geo code coordinate
def coordinates(address, api_key = None):
    url = 'https://maps.googleapis.com/maps/api/geocode/json'

    params = {
        'address' : address.encode('ascii', 'xmlcharrefreplace'),
        'sensor' : 'false'
    }

    if api_key:
        params['key'] = api_key

    response = requests.get(url, params=params)
    coord = response.json()

    if coord['status'] == 'OVER_QUERY_LIMIT':
        raise RuntimeError(coord['error_message'])

    if coord['status'] == 'OK':
        return {
            'lat': coord['results'][0]['geometry']['location']['lat'],
            'lng': coord['results'][0]['geometry']['location']['lng'],
        }
    else:
        return {
            'lat': coord['status'],
            'lng': '',
            }
