from asyncio import events
from urllib import response
from django.http import JsonResponse
import json
from common.json import ModelEncoder
from .acls import get_photo
from django.views.decorators.http import require_http_methods
from .models import Conference, Location, State

class LocationListEncoder(ModelEncoder):
    model = Location
    properties = ["name"]

class ConferenceDetailEncoder(ModelEncoder):
    model = Conference
    properties = [
        "name",
        "description",
        "max_presentations",
        "max_attendees",
        "starts",
        "ends",
        "created",
        "updated",
        "location",
    ]
    encoders = {
            "locations": LocationListEncoder(),
        }

def api_show_conference(request):
    conference = Conference.objects.get(id=id)
    return JsonResponse(
        conference,
        encoder=ConferenceDetailEncoder,
    )

class ConferenceListEncoder(ModelEncoder):
    model = Conference
    properties = ["name"]


def api_list_conferences(request):
    conferences = Conference.objects.all()
    return JsonResponse(
        {"conferences": conferences},
        encoder=ConferenceListEncoder,
    )

class LocationDetailEncoder(ModelEncoder):
    model = Location
    properties = [
        "name",
        "city",
        "room_count",
        "created",
        "updated",
    ]

    def get_extra_data(self, o):
        return {"state":o.state.abbreviation}


@require_http_methods(["DELETE", "GET", "PUT"]) 
def api_show_location(request, id):
  location = Location.objects.get(id=id)
  return JsonResponse(
    location, 
    encoder = LocationDetailEncoder,
    safe=False,
  )

@require_http_methods(["GET", "POST"])
def api_list_locations(request):
    if request.method == "GET":
        locations = Location.objects.get(id=id)
        return JsonResponse(
            {"locations": locations},
        encoder=LocationListEncoder,
        )
    else:
        content = json.loads(request.body)
        state = State.objects.get(abbreviation = content ["state"])
        content["state"] = state
    # except State.DoesNotExist:
    #         return JsonResponse(
    #         {"message": "Invalid state abbreviation"},
    #         status = 400,
        
    class Get_photo():
        photo = get_photo(content["city"], content["state"] )
        content.update(photo)

        location = Location.objects.create(**content)
    return JsonResponse(
        location,
        encoder=LocationDetailEncoder,
        safe=False,
    )


def api_show_location(request, id):
    location = Location.objects.get(id=id)
    return JsonResponse({
        "name": location.name,
        "city": location.city,
        "room_count": location.room_count,
        "created": location.created,
        "updated":location.updated,
        "state":location.state
    }
)
   
