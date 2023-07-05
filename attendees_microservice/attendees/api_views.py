from urllib import response
from django.http import JsonResponse

from .models import Attendee


def api_list_attendees(request, conference_id):
    attendees = Attendee.objects.filter(conference=conference_id)
    return JsonResponse(
        {"attendees": attendees},
        # encoder=AttendeeListEncoder,
    )


def api_show_attendee(request, id):
    attendee = Attendee.objects.get(id=id)
    return JsonResponse(
        {
            "email": attendee.email,
            "name": attendee.name,
            "company_name": attendee.company_name,
            "created": attendee.created,
            "conference": {
                "name": attendee.conference.name,
                "href": attendee.conference.get_api_url(),
            },
        }
    )
