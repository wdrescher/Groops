from django.contrib import admin
from .models import Ride, Featured, Place, Comment, Profile

# Register your models here.
admin.site.register(Ride)
admin.site.register(Featured)
admin.site.register(Place)
admin.site.register(Comment)
admin.site.register(Profile)
