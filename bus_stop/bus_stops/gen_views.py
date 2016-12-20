import requests as req
from django.http import JsonResponse
import json
from geopy.geocoders import GoogleV3
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def geocode_address(request):
    geolocator = GoogleV3()

    if request.method == 'POST':
        location = geolocator.geocode(request.POST.get("address"))
        lat = round(location.latitude, 6)
        lng = round(location.longitude, 6)
        coords = {"lat": lat, "lng": lng}

        return JsonResponse(coords)
    else:
        location = geolocator.geocode(request.GET.get('address'))

        if location != None:
            data = {'validity':1}

            return JsonResponse(data)
        else:
            data = {'validity':0}

            return JsonResponse(data)

def render_landing(request):
    context = {}
    return render(request, 'landing.html', context)
