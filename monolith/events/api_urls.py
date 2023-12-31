from django.urls import path

from .api_views import (
    api_list_conferences,
    api_list_locations,
    api_show_location,
    api_show_conference,
)


urlpatterns = [
    path("conferences/", api_list_conferences, name="api_list_conferences"),
    path("locations/", api_list_locations, name="api_list_locations"),
    path("locations/<int:id>/", api_show_location, name="api_show_location"),
    path(
        "conferences/<int:pk>/",
        api_show_conference,
        name="api_show_conference",
    ),
]
