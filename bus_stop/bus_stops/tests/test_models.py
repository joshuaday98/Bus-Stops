import pytest
from bus_stops.models import NYCStop
pytestmark = pytest.mark.django_db
from fixtures.test_data import test1_busstop, test2_busstop, test_user_loc1, test_address_string, test_user_loc2


class TestNYCStopCreateDestroy:
    def test_NYCStop_creation(self):
        stop = NYCStop.objects.create(**test1_busstop)
        assert stop.stop_id == '301756', 'Did not save an instance.'
        assert stop.type == 'bus'
        assert stop.lat == 40.662807
        assert stop.lng == -73.937302
        assert stop.street == 'TROY AV/EAST NEW YORK AV'

    def test_haversine(self):
        stop1 = NYCStop.objects.create(**test1_busstop)
        stop2 = NYCStop.objects.create(**test2_busstop)

        dist_from_m1 = stop1.find_nearby(test_user_loc1['lat'], test_user_loc1['lng'], test_user_loc1['unit_for_dist'])
        dist_from_ft1 = stop1.find_nearby(test_user_loc2['lat'], test_user_loc2['lng'], test_user_loc2['unit_for_dist'])
        dist_from_m2 = stop2.find_nearby(test_user_loc1['lat'], test_user_loc1['lng'], test_user_loc1['unit_for_dist'])
        dist_from_ft2 = stop2.find_nearby(test_user_loc2['lat'], test_user_loc2['lng'], test_user_loc2['unit_for_dist'])

        assert dist_from_m1 <= test_user_loc1['dist'], 'The result from find_nearby was not less than or equal to the desired distance'
        assert dist_from_ft1 <= test_user_loc1['dist'], 'The result from find_nearby was not less than or equal to the desired distance'
        assert dist_from_m2 >= test_user_loc2['dist'], 'The result from find_nearby was not greater than or equal to the desired distance'
        assert dist_from_ft2 >= test_user_loc2['dist'], 'The result from find_nearby was not greater than or equal to the desired distance'

    def test_coords(self):
        stop1 = NYCStop.objects.create(**test1_busstop)
        stop2 = NYCStop.objects.create(**test2_busstop)

        coords_from1 = stop1.coords()
        coords_from2 = stop2.coords()

        assert coords_from1 == (40.662807, -73.937302), 'The points coordinates were not what they should have been.'
        assert coords_from2 == (40.612453, -74.129768), 'The points coordinates were not what they should have been.'

    def test_repr(self):
        stop1 = NYCStop.objects.create(**test1_busstop)
        stop2 = NYCStop.objects.create(**test2_busstop)

        assert repr(stop1) == 'This stops stats:\nID:301756,\n Street:TROY AV/EAST NEW YORK AV,\n Latitude:40.662807,\n Longitude:-73.937302,\n Type:bus.'
        assert repr(stop2) == 'This stops stats:\nID:905056,\n Street:VICTORY BL / PERRY AV,\n Latitude:40.612453,\n Longitude:-74.129768,\n Type:bus.'

    def test_str(self):
        stop1 = NYCStop.objects.create(**test1_busstop)
        stop2 = NYCStop.objects.create(**test2_busstop)

        assert str(stop1) == '301756, TROY AV/EAST NEW YORK AV'
        assert str(stop2) == '905056, VICTORY BL / PERRY AV'
