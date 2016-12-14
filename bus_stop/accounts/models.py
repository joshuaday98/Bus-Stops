from django.db import models
from django.contrib.auth.models import User
from geopy.geocoders import GoogleV3

class Member(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateTimeField(auto_now=False)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=999)
    last_name = models.CharField(max_length=999)
    gender = models.CharField(max_length=1000)
    home_str = models.CharField(max_length=999)
    home_lat = models.DecimalField(max_digits=9, decimal_places=6)
    home_lng = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.user, self.email

    def __repr__(self):
        pass

    def save(self):
        geocode = GoogleV3()
