from asyncio import events
from urllib import response
from django.http import JsonResponse
import json
from .acls import get_photo

from .models import Conference, Location


def api_list_conferences(request):
    if request.method == "GET":
        conferences = Conference.objects.get(id=id)
        return JsonResponse(
        {"conferences": conferences},
        encoder=ConferenceListEncoder,
    ))
    else:
        content = json.loads(request.body)

    # Get the Location object and put it in the content dict
    try:
        location = Location.objects.get(id=content["location"])
        content["location"] = location
    except Location.DoesNotExist:
        return JsonResponse(
            {"message": "Invalid location id"},
            status=400,
        )

    conference = Conference.objects.create(**content)
    return JsonResponse(
        conference,
        encoder=ConferenceDetailEncoder,
        safe=False,
    )

@require_http_methods(["DELETE", "GET", "PUT"]) 
def api_show_location(request, id):
    if request.method == "GET":
        location = Location.objects.get(id=id)
        return JsonResponse(
        location,
        encoder=LocationDetailEncoder,
        safe=False,)
    else:
    # copied from create
        content = json.loads(request.body)
    try:
        # new code
        if "state" in content:
            state = State.objects.get(abbreviation=content["state"])
            content["state"] = state
    except State.DoesNotExist:
        return JsonResponse(
            {"message": "Invalid state abbreviation"},
            status=400,
        )

    # new code
    Location.objects.filter(id=id).update(**content)

    # copied from get detail
    location = Location.objects.get(id=id)
    return JsonResponse(
        location,
        encoder=LocationDetailEncoder,
        safe=False,
    )
    elif request.method == "DELETE":
        count, _ = Location.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})


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
    except State.DoesNotExist:
        return JsonResponse(
            {"message": "Invalid state abbreviation"},
            status = 400,
        )
        # Get photo
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
return JsonResponse({"location", response})
