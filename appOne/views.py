from django.shortcuts import render
from django.http import HttpResponse
from appOne.models import Ride, Featured, Place
from django.db.models import Q
from location_field.models.plain import PlainLocationField
import datetime
import operator
import requests
from openpyxl import load_workbook, Workbook
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget
from math import sin, cos, sqrt, atan2, radians



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

#
# MAP_WIDGETS = {
#     "GooglePointFieldWidget": (
#         ("zoom", 15),
#         ("mapCenterLocation", [57.7177013, -16.6300491]),
#     ),
#     "GOOGLE_MAP_API_KEY": "<google-map-api-key>"
# }

# Create your views here.
numFeaturedRides = 3 #Able to change this value

# Standard landing page that will display to all users accessing base URL
def index(request):
    template = 'appOne/landpage.html'
    key = Ride.objects.order_by('location')
    feat = Featured.objects
    # for i in range(numFeaturedRides):
    #     feat.insert(Featured.objects.get(f_ride_code=i))

    #feat.insert(Featured.objects.get(0,f_ride_code=1))
    context= {
        'rides':key,
        'featured': feat
    }
    return render(request, template, context)



# Redirected from the land page, this will display after a search
def result(request):
    query = request.GET.get('loc_query').lower()
    d = request.GET.get('radius')
    template = 'appOne/resultBrief.html'

    # Converts queried location to coordinate
    new_location = coordinates(query, 'AIzaSyAQfOibV5klraxtdVGqwlzNiZdpKPm3h-Y')

    # Takes given tuple and converts to array of real
    loc_array = [float(new_location['lat']), float(new_location['lng'])]

    # Gathers all Rides, and iterates checking for distance
    all_rides = Ride.objects.all()
    rides_in_range = []
    for r in all_rides:
        ride_loc = r.f_location_name.location_name
        ride_array = [float(ride_loc.split(',')[0]), float(ride_loc.split(',')[1])]
        if ( distance(loc_array, ride_array) <= int(d)):
            rides_in_range.insert(0, r)



    context = {
        # 'rides': rides_in_range, temporarily out: this queryset will only contain rides that are within range

        'rides': rides_in_range,
        'recentSearch': query,
        'd': d
        # 'query':Ride.objects.filter(comments=query) used to display queryset during testing
    }

    return render(request, template, context)


# Upon clicking on each of the ride briefs, the detailed view will open
def detail(request, pk):
    template = 'appOne/detailedReport.html'
    MAP_WIDGETS = {
        "GooglePointFieldWidget": (
            ("zoom", 15),
            ("mapCenterLocation", [57.7177013, -16.6300491]),
        ),
        "GOOGLE_MAP_API_KEY": "<google-map-api-key>"
    }
    context = {
        'ride': Ride.objects.filter(id=pk),
        'place': Place.objects.filter(id = pk),
        'widget': GooglePointFieldWidget
    }
    return render(request, template, context)
