from django.forms import ModelForm
from .models import Ride

class inRide(ModelForm):
    class Meta:
        model = Ride

        fieds = [distance, start_time, pace, location, route
                 num_participants, start_date, end_date,
                 strava_link, comments, road_surfaces,
                 contact_number, ride_code]
