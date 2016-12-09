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


    for stop in NYCStop.objects.all():
        result = stop.find_nearby(inc_lat,
                                  inc_lng,

                                  request.POST['unit_for_dist'])

        if result <= float(request.POST['dist']):
            local_points[stop.stop_id] = {'lat':str(stop.lat),
                                          'lng':str(stop.lng),
                                          'type':stop.type,
                                          'street':stop.street}

    local_points = json.loads(json.dumps(local_points))

    return JsonResponse(local_points)

def post_nyc(request):
    context = {'city':'NYC'}
    return render(request, 'main.html', context)
