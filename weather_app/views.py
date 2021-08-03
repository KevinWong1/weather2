from django.shortcuts import render
import requests
import datetime
import os


def index(request):

    OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
    # e48e0a2d37211056d27243de4d6d61eb

    api_key = os.environ.get("OWM_API_KEY")
    lat = "37.804829"
    lon = "-122.272476"
    time = datetime.datetime.now()
    weather_params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "exculde": "current,minutely,daily"
    }

    response = requests.get(OWM_Endpoint, params=weather_params)
    weather_data = response.json()
    context = {
        "weather": weather_data["current"]["weather"][0]["main"],
        "time": time
    }

    # print(context["weather"])
    return render(request, 'weather_app/index.html', context)
