from django.db import models
from django.db import models
from location_field.models.plain import PlainLocationField

class Place(models.Model):
    city = models.CharField(max_length=255)
    location_name = PlainLocationField(based_fields=['city'], zoom=7)

    def __str__(self):
        return self.city

#We could potentially divide this table into location/city with each ride
class Ride(models.Model):
    distance = models.IntegerField()
    start_time = models.TimeField()
    pace = models.IntegerField()
    ride_name = models.CharField(max_length=100)
    route = models.CharField(max_length=300) #I am currently unsure how to integrate strava route, could be a simple tcx file
    num_participants = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    strava_link = models.CharField(max_length=300)
    comments = models.CharField(max_length=250)
    road_surfaces = models.CharField(max_length=250)
    contact_number = models.CharField(max_length=10)
    f_location_name = models.ForeignKey('Place', on_delete=models.CASCADE, default='1')

    def findDay(self):
        WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        num = self.start_date.weekday()
        return WEEKDAYS[num]


    def __str__(self):
        return (self.ride_name)


#ride code will be limited, and have a range of 0-5
class Featured(models.Model):
    f_ride_code = models.ForeignKey('Ride', on_delete=models.CASCADE)

    def __str__(self):
        return self.f_ride_code
