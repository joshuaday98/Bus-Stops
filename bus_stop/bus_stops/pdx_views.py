from django.shortcuts import render
from private.secrets import TRIMET
import requests as req
from django.http import JsonResponse
import json
from geopy.geocoders import GoogleV3
from django.views.decorators.csrf import csrf_exempt


def post_pdx(request):
    context = {'city':'PDX'}
    return render(request, 'main.html', context)


@csrf_exempt
def find_route(request):
    if request.method == 'POST':
        route_num = request.POST['route']

        url = 'https://developer.trimet.org/ws/v2/vehicles'
        data = {'appID': TRIMET,
                'routes': route_num,
                'json': 'true'}

        response = req.get(url, data)
        return JsonResponse(response.json())


@csrf_exempt
def find_stops(request):
    if request.method == 'POST':
        lat = request.POST['lat']
        lng = request.POST['lng']
        dist = request.POST['distance']
        dist_unit = request.POST['unit_for_dist'].lower()
        laln = lat + ',' + lng

        url = 'https://developer.trimet.org/ws/V1/stops/'
        data = {'json': 'true',
                'appID': TRIMET,
                'll': laln,
                dist_unit: dist,
                'showRoutes': 'true'}

        response = req.get(url, data)

        return JsonResponse(response.json(), safe=False)
