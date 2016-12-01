import pytest
from mixer.backend.django import mixer
from bus_stops.models import NYCStop
pytestmark = pytest.mark.django_db


class TestPost:
    def test_NYCStop(self):
        stop = mixer.blend('bus_stops.NYCStop', stop_id='A106N')
        assert stop.stop_id == 'A106N', 'Should save an instance'
