from django.shortcuts import render


def post_nyc(request):
    context = {'city':'NYC'}
    return render(request, 'main.html', context)
