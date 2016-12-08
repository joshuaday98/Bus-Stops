from django.shortcuts import render
from django.http import JsonResponse
import json
from math import *
from bus_stops.models import NYCStop
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def find_stops(request):
    local_points = {}
    inc_lat = float(request.POST['lat'])
    inc_lng = float(request.POST['lng'])

    if request.POST['unit_for_dist'] == 'ft':
        r = 3956 # radius of earth in miles
    else:
        r = 6371 # radius of earth in km

    for stop in NYCStop.objects.all():
        stop_lat, stop_lng = stop.coords()[0], stop.coords()[1]

        """
        HAVERSINE FORMULA
        """
        inc_lat_rad, inc_lng_rad, stop_lat_rad, stop_lng_rad = map(radians, [inc_lat, inc_lng, stop_lat, stop_lng])

        dlon = stop_lng_rad - inc_lng_rad
        dlat = stop_lat_rad - inc_lat_rad
        a = sin(dlat / 2) ** 2 + cos(inc_lat_rad) * cos(stop_lat_rad) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        result = c * r

        if request.POST['unit_for_dist'] == 'ft':
            result = result * 5280
        else:
            result = result * 1000

        if result <= float(request.POST['dist']):
            local_points[stop.stop_id] = {'lat':str(stop_lat),
                                          'lng':str(stop_lng),
                                          'type':stop.type,
                                          'street':stop.street}

    local_points = json.loads(json.dumps(local_points))

    """
    TODO: turn the stop into a dictionary stop_id:(lat, lng)
    """
    return JsonResponse(local_points)

def post_nyc(request):
    context = {'city':'NYC'}
    return render(request, 'main.html', context)
