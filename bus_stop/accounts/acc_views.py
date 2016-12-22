from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import Member
from geopy.geocoders import GoogleV3
import json
from django.contrib.auth import authenticate, login
from django.contrib import messages


def create_acc(request):
    if request.method == 'POST':
        context = {}
        username = request.POST.get('email').split('@')[0]
        home_str = request.POST.get('street') + ', ' + request.POST.get('city') + ', ' + request.POST.get('state') + ' ' + request.POST.get('zip')
        password = request.POST.get('password')
        geocoder = GoogleV3()

        if geocoder.geocode(home_str) is None:
            context['error'] = 'Not valid Address'
            response = HttpResponse(json.dumps(context))
            response.status_code = 400
            return response

        querydict = {'email':request.POST.get('email'),
                     'first_name':request.POST.get('fname'),
                     'last_name':request.POST.get('lname'),
                     'gender':request.POST.get('gender'),
                     'home_str':home_str}

        user = User.objects.create(username=username, password=password)
        member = Member.objects.create(user=user, **querydict)

        user.save()
        member.save()

        user_login = authenticate(username=username, password=password)

        if user_login is not None:
            login(request, user)

            return render(request, 'landing.html', context)

    return


def login_acc(request):
    if request.method == 'POST':
        context = {}
        username = request.POST.get('email').split('@')[0]
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            context['message'] ='Successfully logged in!'

            return render(request, 'landing.html', context)

        else:
            response = HttpResponse
            response.status_code = 401
            return HttpResponse
