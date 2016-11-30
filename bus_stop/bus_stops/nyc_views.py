from django.shortcuts import render


def post_nyc(request):
    context = {}
    return render(request, 'nyc.html')
