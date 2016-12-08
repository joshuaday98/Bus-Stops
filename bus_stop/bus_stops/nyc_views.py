from django.shortcuts import render
from django.http import JsonResponse
import json
from math import *
from bus_stops.models import NYCStop
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def find_stops(request):
    local_points = []
    inc_lat = float(request.POST['lat'])
    inc_lng = float(request.POST['lng'])

    if request.POST['unit_for_dist'] == 'ft':
        r = 3956 # radius of earth in miles
    else:
        r = 6371 # radius of earth in km

    for stop in NYCStop.objects.all():
        stop_coords = stop.coords()
        stop_lat, stop_lng = stop_coords()[0], stop_coords()[1]

        """
        HAVERSINE FORMULA
        """
        inc_lat, inc_lng, stop_lat, stop_lng = map(radians, [inc_lat, inc_lng, stop_lat, stop_lng])

        dlon = stop_lng - inc_lng
        dlat = stop_lat - inc_lat
        a = sin(dlat / 2) ** 2 + cos(inc_lat) * cos(stop_lat) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        result = c * r

        if request.POST['unit_for_dist'] == 'ft':
            result = result * 5280
        else:
            result = result * 1000

        if result <= request.POST['dist']:
            local_points.append(result)
        """
        TODO: turn the stop into a dictionary stop_id:(lat, lng)
        """

def post_nyc(request):
    context = {'city':'NYC'}
    return render(request, 'main.html', context)
