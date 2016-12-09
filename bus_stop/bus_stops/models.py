from django.db import models
from math import *

class NYCStop(models.Model):
    """

    """
    stop_id = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    type = models.CharField(max_length=3)

    class Meta:
        unique_together = ['stop_id', 'lat', 'lng']

    def __str__(self):
        result = '{}, {}'.format(self.stop_id, self.street)
        return result

    def __repr__(self):
        print(self.stop_id)
        print(self.street)
        print(self.lat)
        print(self.lng)
        print(self.type)
        return 'There are your stats!'

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
