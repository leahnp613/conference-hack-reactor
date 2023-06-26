from django.http import JsonResponse

from .models import Presentation


def api_list_presentations(request, conference_id):
    """
    Lists the presentation titles and the link to the
    presentation for the specified conference id.

    Returns a dictionary with a single key "presentations"
    which is a list of presentation titles and URLS. Each
    entry in the list is a dictionary that contains the
    title of the presentation, the name of its status, and
    the link to the presentation's information.

    {
        "presentations": [
            {
                "title": presentation's title,
                "status": presentation's status name
                "href": URL to the presentation,
            },
            ...
        ]
    }
    """
    presentations = [
        {
            "title": p.title,
            "status": p.status.name,
            "href": p.get_api_url(),
        }
        for p in Presentation.objects.filter(conference=conference_id)
    ]
    return JsonResponse({"presentations": presentations})


def api_show_presentation(request, id):
   presentation = Presentation.objects.get(id=id)
   return JsonResponse(
    {
        "presenter_name": presentation.presenter_name,
        "company_name": presentation.company_name,
       "presenter_email": presentation.presenter_email,
        "title": presentation.title,
        "synopsis": presentation.synopsis,
        "created": presentation.created,
        "status":presentation.status,
        "conference":{
            "name": presentation.conference.name,
            "href": presentation.get_api_url(),
        }
    }
)
