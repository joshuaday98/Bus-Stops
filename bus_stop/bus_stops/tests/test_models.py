import pytest
from mixer.backend.django import mixer
from bus_stops.models import NYCStop
pytestmark = pytest.mark.django_db
from fixtures.test_data import test1_busstop, test2_busstop,test_user_loc, test_address_string


class TestNYCStopCreateDestroy:
    def test_NYCStop_creation(self):
        stop = NYCStop.objects.create(**test1_busstop)
        assert stop.stop_id == '301756', 'Did not save an instance.'
        assert stop.type == 'bus'
        assert stop.lat == 40.662807
        assert stop.lng == -73.937302
        assert stop.street == 'TROY AV/EAST NEW YORK AV'

class TestNYCStopGeoOperations:
    def test_haversine(self):
        stop1 = NYCStop.objects.create(**test1_busstop)
        stop2 = NYCStop.objects.create(**test2_busstop)

        dist_from1 = stop1.find_nearby(test_user_loc['lat'], test_user_loc['lng'], test_user_loc['unit_for_dist'])
        dist_from2 = stop2.find_nearby(test_user_loc['lat'], test_user_loc['lng'], test_user_loc['unit_for_dist'])

        assert dist_from1 <= test_user_loc['dist']
        assert dist_from2 >= test_user_loc['dist']
