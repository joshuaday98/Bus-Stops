from django.shortcuts import render
from private.secrets import TRIMET
import requests as req
from django.http import JsonResponse
import json


def post_page(request):
    context = {}
    return render(request, 'bus_stop.html')


def find_stops(request):
    if request.method == 'POST':
        lat = request.POST['lat']
        lng = request.POST['lng']
        laln = lat + ',' + lng

        url = 'https://developer.trimet.org/ws/V1/stops/'
        data = {'json': 'true', 'appID': TRIMET, 'll': laln, 'meters': '275', 'showRoutes':'true'}
        response = req.get(url, data)
        response = json.loads(response.text)

        return JsonResponse(response, safe=False)
# Create your views here.
