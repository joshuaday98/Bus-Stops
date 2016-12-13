from django.test import RequestFactory
import pytest
from bus_stops.nyc_views import *
import json


class TestNYCViews:
    def test_post_nyc(self):
        request = RequestFactory().get('/')
        response = post_nyc(request)

        assert response.status_code == 200, 'Should be callable by anyone'

    def test_find_stops(self):
        data = {'lat':40.6624270, 'lng':-73.9369330, 'dist':220, 'dist_unit': 'ft'}
        request = RequestFactory().post('/', data=data)
        response = find_stops(request)
        response_details = json.loads(str(response.getvalue()))

        


        assert response.status_code == 200, 'Should be accesible by anybody.'
        assert response_details[0].lat == 40.662807, 'Does not return correct lat.'
        assert response_details[0].lng == -73.937302, 'Does not return correct lng.'
