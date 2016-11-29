from django.db import models


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
