from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Member
from geopy.geocoders import GoogleV3


def create_acc(request):
    if request.method == 'POST':
        username = request.POST.get('email').split('@')[0]
        home_str = request.POST.get('street') + ' ' + request.POST.get('state') + ' ' + request.POST.get('zip')

        querydict = {'user':username,
                     'password':request.POST.get('password'),
                     'email':request.POST.get('email'),
                     'first_name':request.POST.get('fname'),
                     'last_name':request.POST.get('lname'),
                     'gender':request.POST.get('gender'),
                     'home_str':home_str}

        user = User.objects.create(username=username, password=password)
        member = Member.objects.create(user=user, **querydict)

        user.save()
        member.save()

    context = {}

    return render(request, 'acct/acct_create.html', context)
