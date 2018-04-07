from django.db import models
from django.contrib.auth.models import User
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

# Users will have the ability to create comments, and potentially rides
# Users are imported from django to include their functionality
    # username
    # password ENCRYPTED
    # email
    # first_name
    # last_name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    friend_id = models.ForeignKey('Profile', on_delete=models.CASCADE)

#comments will be associated to one ride, with one user, both users and rides can have multiple comments
class Comment(models.Model):
    title = models.CharField(max_length = 100)
    body = models.CharField(max_length = 500)
    date = models.DateField()
    f_user = models.ForeignKey('Profile', on_delete=models.CASCADE, default = '1')
    f_ride = models.ForeignKey('Ride', on_delete=models.CASCADE, default= '1')
