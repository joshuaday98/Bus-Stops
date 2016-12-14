import requests as req
from django.http import JsonResponse
import json
from geopy.geocoders import GoogleV3
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from accounts.forms import MemberRegistrationForm
from django.contrib.auth.forms import UserCreationForm

@csrf_exempt
def geocode_address(request):
    if request.method == 'POST':
        geolocator = GoogleV3()
        location = geolocator.geocode(request.POST.get("address"))
        lat = round(location.latitude, 6)
        lng = round(location.longitude, 6)
        coords = {"lat": lat, "lng": lng}

        return JsonResponse(coords)


def render_landing(request):
    context = {}
    return render(request, 'landing.html', context)
