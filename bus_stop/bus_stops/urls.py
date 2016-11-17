from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_page, name='post_page'),
    url(r'^find_stops/', views.find_stops, name='find_stops'),
]
