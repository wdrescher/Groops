from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth import login, authenticate

import datetime
import operator

from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget
from location_field.models.plain import PlainLocationField

from .models import Ride, Featured, Place
from .coordinateFunctions import distance, coordinates

# Create your views here.


# Standard landing page that will display to all users accessing base URL
def index(request):
    template = 'grouprides/landpage.html'
    key = Ride.objects.order_by('location')
    feat = Featured.objects

    context= {
        'rides':key,
        'featured': feat
    }
    return render(request, template, context)

# Redirected from the land page, this will display after a search
def result(request):
    query = request.GET.get('loc_query').lower()
    d = request.GET.get('radius')
    template = 'grouprides/resultBrief.html'

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
    template = 'grouprides/detailedReport.html'
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
