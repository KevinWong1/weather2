from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = "weather_app"

urlpatterns = [
    path('', views.index, name='index')
]
