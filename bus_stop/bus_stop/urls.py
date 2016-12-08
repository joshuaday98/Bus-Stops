"""bus_stop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from bus_stops import pdx_views, nyc_views, gen_views
from django.conf import settings

urlpatterns = [
    # urls user can actually use
    url(r'^admin/', admin.site.urls),
    url(r'^pdx/', pdx_views.post_pdx, name='post_pdx'),
    url(r'^nyc/', nyc_views.post_nyc, name='post_nyc'),

    # PDX Views functions
    url(r'^find_stops/', pdx_views.find_stops, name='find_stops'),
    url(r'^find_route/', pdx_views.find_route, name='find_route'),
    url(r'^geocode/', gen_views.geocode_address, name='geocode_address'),

    # NYC Views functions
    url(r'^nyc_find_stops/', nyc_views.find_stops, name='find_stops')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
