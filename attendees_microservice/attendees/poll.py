import json
import requests

from .models import ConferenceVO


def get_conferences():
    response = requests.get("http://monolith:8000/api/conferences/")
    content = json.loads(response.content)
    for conference in content["conferences"]:
        ConferenceVO.objects.update_or_create(
            import_href=conference["href"],
            defaults={"name": conference["name"]},
        )
