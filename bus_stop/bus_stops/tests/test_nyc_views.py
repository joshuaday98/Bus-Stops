from django.test import RequestFactory

from bus_stops.nyc_views import *


class TestNYCViews:
    def test_post_nyc(self):
        request = RequestFactory().get('/')
        response = post_nyc(request)

        assert response.status_code == 200, 'Should be callable by anyone'
