from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY
from django.http import JsonResponse
import requests
import json


def get_photo(city,state):
    headers = {"Authorization": PEXELS_API_KEY}
    params = {
        "per_page":1,
        "query": f"{city} {state}"
    }
    url = "https://api.pexels.com/v1/search"

    response = requests.get(url, params = params, headers = headers)
    content = json.loads(response.content)
    print(content)

    try:
        return {"picture_url": content["photos"] [0] ["src"]["original"]}
    except (KeyError, IndexError):
        return{"picture_url": None}

    





def get_weather_data(city, state):
    headers = {"Authorization": OPEN_WEATHER_API_KEY}
    params = {
            "appid":OPEN_WEATHER_API_KEY,
            "q": f"{city} {state}",
            "limit": 1
        }
    url = "http://api.openweathermap.org/geo/1.0/direct"

    response = requests.get(url, params = params, headers = headers)
    content = json.loads(response.content)
    try:
            return {"name": content["name"]["state"]["lat"]["lon"]["country"]}
    except (KeyError, IndexError):
            return{"name": None}

    print(content)
        