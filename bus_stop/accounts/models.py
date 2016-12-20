from django.db import models
from django.contrib.auth.models import User
from geopy.geocoders import GoogleV3


class Member(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=999)
    last_name = models.CharField(max_length=999)
    gender = models.CharField(max_length=999)
    home_str = models.CharField(max_length=999)
    home_lat = models.DecimalField(max_digits=9, decimal_places=6)
    home_lng = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.user, self.email

    def __repr__(self):
        return "{}, {}".format(self.user, self.email)

    def save(self, force_insert=False, force_update=False, using=None, *args, **kwargs):
        geocoder = GoogleV3()
        location = geocoder.geocode(self.home_str)

        self.home_lat = round(location.latitude, 6)
        self.home_lng = round(location.longitude, 6)

        super(Member, self).save(*args, **kwargs)
