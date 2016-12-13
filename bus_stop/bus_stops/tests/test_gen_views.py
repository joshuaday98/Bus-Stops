from django.test import RequestFactory
import json
from bus_stops.gen_views import *
import pytest


class TestGenViews:
    def test_geocode_address(self):
        data = {'address':'160 SE Oak St.'}
        request = RequestFactory().post('/', data=data)
        response = geocode_address(request)
        response_details = json.loads(str(response.getvalue()))

        assert response.status_code == 200, 'Should be accessible by anyone.'
        assert response_details.lat == '45.518858', 'Incorrect latitude.'
        assert response_details.lng == '-122.988641', 'Incorrect longitude.'
