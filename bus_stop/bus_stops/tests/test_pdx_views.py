from django.test import RequestFactory

from bus_stops.pdx_views import *


class TestPDXViews:
    def test_post_pdx(self):
        request = RequestFactory().get('/')
        response = post_pdx(request)

        assert response.status_code == 200, 'Should be callable by anyone.'
