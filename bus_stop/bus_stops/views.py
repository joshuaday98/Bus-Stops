from django.shortcuts import render
from private.secrets import TRIMET
import requests as req
from django.http import JsonResponse
import json
from geopy.geocoders import GoogleV3


def post_page(request):
    context = {}
    return render(request, 'bus_stop.html')


def find_route(request):
    if request.method == 'POST':
        route_num = request.POST['route']

        url = 'https://developer.trimet.org/ws/v2/vehicles'
        data = {'appID': TRIMET, 'routes': route_num}

        response = req.get(url, data)
        return JsonResponse(response.json())


def find_stops(request):
    if request.method == 'POST':
        lat = request.POST['lat']
        lng = request.POST['lng']
        laln = lat + ',' + lng

        url = 'https://developer.trimet.org/ws/V1/stops/'
        data = {'json': 'true',
                'appID': TRIMET,
                'll': laln,
                'meters': '275',
                'showRoutes': 'true'}

        response = req.get(url, data)
        response = json.loads(response.text)

        return JsonResponse(response, safe=False)


def geocode_address(request):
    if request.method == 'POST':
        geolocator = GoogleV3()
        location = geolocator.geocode(request.POST.get("address"))
        lat = location.latitude
        lng = location.longitude
        coords = {"lat": lat, "lng": lng}

        return JsonResponse(coords)
