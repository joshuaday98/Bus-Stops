from django.shortcuts import render
from django.http import JsonResponse
import json
from math import *
from bus_stops.models import NYCStop
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def find_stops(request):
    lat = float(request.POST['lat'])
    lng = float(request.POST['lng'])

    if request.POST['unit_for_dist'] == 'ft':
        dist = float(request.POST['dist'] * 0.3048)
    else:
        dist = float(request.POST['dist'])

    """
    Finds the max coords to compare every stop from the database to.
    if all conditions met the point will be plotted on the map!
    """

    lat_max = round(lat + (dist/110574), 6)
    lat_min = round(lat - (dist/110574), 6)
    lng_max = round(lng + ((dist/110574) * cos(lat)), 6)
    lng_min = round(lng - ((dist/110574) * cos(lat)), 6)

    nycstops = NYCStop.objects.filter(lat__lte=lat_max)\
                              .filter(lat__gte=lat_min)\
                              .filter(lng__lte=lng_max)\
                              .filter(lng__gte=lng_min)

    import pdb; pdb.set_trace()


def post_nyc(request):
    context = {'city':'NYC'}
    return render(request, 'main.html', context)
