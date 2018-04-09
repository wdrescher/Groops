from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from groop.grouprides.models import Ride
# Create your models here.

# Users will have the ability to create comments, and potentially rides
# Users are imported from django to include their functionality
    # username
    # password ENCRYPTED
    # email
    # first_name
    # last_name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=50, default='test')
    l_name = models.CharField(max_length=100, default='User')
    bio = models.TextField(max_length=500, blank=True, null=True)
    friend_id = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True, blank=True)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
    def __str__(self):
        return self.l_name + ', ' + self.f_name

#comments will be associated to one ride, with one user, both users and rides can have multiple comments
class Comment(models.Model):
    title = models.CharField(max_length = 100)
    body = models.CharField(max_length = 500)
    date = models.DateField()
    f_user = models.ForeignKey('Profile', on_delete=models.CASCADE, default = '1')
    f_ride = models.ForeignKey(Ride, on_delete=models.CASCADE, default= '1')
