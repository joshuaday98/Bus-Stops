from django.db import models
from math import *
from geopy.geocoders import GoogleV3

class NYCStop(models.Model):
    """

    """
    stop_id = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    type = models.CharField(max_length=3)

    class Meta:
        unique_together = ['stop_id', 'lat', 'lng', 'type', 'street']

    def __str__(self):
        result = '{}, {}'.format(self.stop_id, self.street)
        return result

    def __repr__(self):
        result = 'This stops stats:\nID:{},\n Street:{},\n Latitude:{},\n Longitude:{},\n Type:{}.'.format(self.stop_id, self.street, self.lat, self.lng, self.type)
        return result

    def coords(self):
        result = (self.lat, self.lng)
        return result

    def find_nearby(self, in_lat, in_lng, dist_unit):
        stop_lat, stop_lng = self.lat, self.lng
        in_lat, in_lng, stop_lat, stop_lng = map(radians, [in_lat, in_lng, stop_lat, stop_lng])

        if dist_unit == 'ft':
            r = 3956
        else:
            r = 6371

        """
        Haversine formula! Would write more about it but I am not good enough
        at math to understand!
        """
        dlon = stop_lng - in_lng
        dlat = stop_lat - in_lat
        a = sin(dlat / 2) ** 2 + cos(in_lat) * cos(stop_lat) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        result = c * r

        if dist_unit == 'ft':
            result = result * 5280
        else:
            result = result * 1000

        return result

    def human_address(self):
        geolocator = GoogleV3()
        location = geolocator.reverse((str(self.lat),str(self.lng)), exactly_one=True)
        pretty_address = location.address.split(' ')[0:-2:]
        pretty_address = ' '.join(pretty_address)
        return pretty_address
